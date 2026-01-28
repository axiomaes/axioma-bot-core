from pydantic import BaseModel

class ChatwootResponse(BaseModel):
    content: str
    action: str = "reply" # reply, private_note, etc.
