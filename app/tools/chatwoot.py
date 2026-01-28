import httpx
from app.config.settings import get_settings
from app.utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

class ChatwootClient:
    def __init__(self):
        self.base_url = settings.CHATWOOT_BASE_URL
        self.api_token = settings.CHATWOOT_API_TOKEN

    async def send_message(self, conversation_id: int, content: str, message_type: str = "outgoing"):
        if not self.base_url or not self.api_token:
            logger.warning("Chatwoot config missing, skipping message send.")
            return
        
        url = f"{self.base_url}/api/v1/conversations/{conversation_id}/messages"
        headers = {"api_access_token": self.api_token}
        payload = {
            "content": content,
            "message_type": message_type,
            "private": False
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=payload)
                response.raise_for_status()
                logger.info(f"Message sent to Chatwoot conversation {conversation_id}")
            except Exception as e:
                logger.error(f"Failed to send message to Chatwoot: {e}")
