import httpx
from app.config.settings import get_settings
from app.utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

class N8NClient:
    def __init__(self):
        self.webhook_url = settings.N8N_WEBHOOK_URL

    async def trigger_workflow(self, workflow_id: str, payload: dict):
        if not self.webhook_url:
            logger.warning("N8N webhook URL not set.")
            return None
            
        url = f"{self.webhook_url}/{workflow_id}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Failed to trigger n8n workflow: {e}")
                return None
