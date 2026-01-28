from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any

class Sender(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

class Conversation(BaseModel):
    id: int
    inbox_id: int
    status: Optional[str] = None

class WebhookPayload(BaseModel):
    event: str
    id: Optional[int] = None
    content: Optional[str] = None
    message_type: Optional[str] = None # incoming, outgoing
    private: bool = False
    sender: Optional[Sender] = None
    conversation: Optional[Conversation] = None
    account: Optional[Dict[str, Any]] = None
    
    # Allow extra fields since Chatwoot webhooks can vary
    model_config = {
        "extra": "ignore"
    }
