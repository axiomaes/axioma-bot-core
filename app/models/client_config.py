from pydantic import BaseModel
from typing import Optional

class ClientConfig(BaseModel):
    client_id: str
    name: str
    api_key: Optional[str] = None
    workflow_id: str = "default"
    # Specific provider settings can go here
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o"
