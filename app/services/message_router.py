from app.models.message import Message
from app.models.client_config import ClientConfig
from typing import Optional

class MessageRouter:
    def get_client_config(self, inbox_id: str) -> Optional[ClientConfig]:
        # Placeholder: Map inbox_id to ClientConfig
        # In production this would fetch from DB or Axioma Core
        if inbox_id == "1":
            return ClientConfig(client_id="clientA", name="Client A", workflow_id="clientA")
        elif inbox_id == "2":
            return ClientConfig(client_id="clientB", name="Client B", workflow_id="clientB")
        return ClientConfig(client_id="default", name="Default", workflow_id="default")

    async def route(self, message: Message) -> str:
        # Determine which workflow to use
        config = self.get_client_config(message.inbox_id)
        return config.workflow_id
