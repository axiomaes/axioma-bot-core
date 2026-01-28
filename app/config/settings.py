import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Axioma Bot Core"
    DEBUG: bool = False
    
    # API Keys & Secrets
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    CHATWOOT_API_TOKEN: str | None = None
    CHATWOOT_BASE_URL: str | None = None
    AXIOMA_CORE_API_KEY: str | None = None
    AXIOMA_CORE_BASE_URL: str | None = None
    
    # N8N Config
    N8N_WEBHOOK_URL: str | None = None

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore"
    }

@lru_cache()
def get_settings():
    return Settings()
