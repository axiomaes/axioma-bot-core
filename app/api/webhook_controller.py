from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.schemas.webhook_payload import WebhookPayload
from app.graph.base_graph import BaseGraph
from app.models.message import Message
from app.tools.chatwoot import ChatwootClient
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)

# Initialize graph (singleton or per-request depending on design, here simple singleton)
agent_graph = BaseGraph()
chatwoot_client = ChatwootClient()

async def process_message_task(message: Message):
    try:
        response_text = await agent_graph.run(message)
        # Send back to Chatwoot
        await chatwoot_client.send_message(
            conversation_id=int(message.conversation_id),
            content=response_text
        )
    except Exception as e:
        logger.error(f"Error processing message: {e}")

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
