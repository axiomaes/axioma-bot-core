from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.schemas.webhook_payload import WebhookPayload
from app.graph.base_graph import BaseGraph
from app.models.message import Message
from app.tools.chatwoot import ChatwootClient
from app.utils.logger import setup_logger
from app.services.message_router import MessageRouter

router = APIRouter()
logger = setup_logger(__name__)

from app.services.execution_store import get_execution_store

# Initialize graph (singleton or per-request depending on design, here simple singleton)
agent_graph = BaseGraph()
chatwoot_client = ChatwootClient()
store = get_execution_store()

async def process_message_task(message: Message):
    # Determine workflow name - simpler logic for now
    router_service = MessageRouter() # Need to init this one
    workflow_id = await router_service.route(message)
    
    # Start execution record
    exec_id = store.add_execution(
        client_id=workflow_id, # Using workflow_id as client_id proxy for scaffold
        workflow_name=workflow_id,
        input_message=message.content
    )
    
    try:
        response_text, steps = await agent_graph.run(message)
        
        # Update execution record
        store.update_execution(
            execution_id=exec_id,
            output_message=response_text,
            steps=steps
        )
        
        # Send back to Chatwoot
        await chatwoot_client.send_message(
            conversation_id=int(message.conversation_id),
            content=response_text
        )
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        store.update_execution(
            execution_id=exec_id,
            output_message=f"Error: {str(e)}",
            steps=[{"error": str(e)}]
        )

@router.post("/webhook/chatwoot")
async def chatwoot_webhook(payload: WebhookPayload, background_tasks: BackgroundTasks):
    logger.info(f"Received webhook event: {payload.event}")
    
    if payload.event == "message_created" and payload.message_type == "incoming" and not payload.private:
        if not payload.content:
            return {"status": "ignored", "reason": "empty content"}
            
        message = Message(
            id=str(payload.id),
            content=payload.content,
            sender_id=str(payload.sender.id) if payload.sender else "unknown",
            conversation_id=str(payload.conversation.id) if payload.conversation else "unknown",
            inbox_id=str(payload.conversation.inbox_id) if payload.conversation else "unknown",
            account_id=str(payload.account.get("id", "unknown")) if payload.account else "unknown"
        )
        
        # Run agent in background to return 200 OK immediately
        background_tasks.add_task(process_message_task, message)
        return {"status": "processing"}
    
    return {"status": "ignored", "reason": "not an incoming message"}
