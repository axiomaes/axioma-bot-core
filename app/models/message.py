from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class Message(BaseModel):
    id: str
    content: str
    sender_id: str
    conversation_id: str
    inbox_id: str
    account_id: str
    message_type: str = "incoming" # incoming or outgoing
    metadata: Dict[str, Any] = Field(default_factory=dict)
