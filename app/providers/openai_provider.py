from .llm_provider import LLMProvider
from langchain_openai import ChatOpenAI
from app.config.settings import get_settings
from typing import List, Dict

settings = get_settings()

class OpenAIProvider(LLMProvider):
    def __init__(self, model_name: str = "gpt-4o"):
        self.client = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=model_name
        )

    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        # Simplified for now, usually needs conversion of messages format
        # LangChain handles dicts well usually or needs specific Message objects
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
        
        lc_messages = []
        for msg in messages:
            role = msg.get("role")
            content = msg.get("content")
            if role == "system":
                lc_messages.append(SystemMessage(content=content))
            elif role == "user":
                lc_messages.append(HumanMessage(content=content))
            elif role == "assistant":
                lc_messages.append(AIMessage(content=content))
                
        response = await self.client.ainvoke(lc_messages)
        return response.content
