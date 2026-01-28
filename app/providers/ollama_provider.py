from .llm_provider import LLMProvider
from langchain_community.chat_models import ChatOllama
from typing import List, Dict

class OllamaProvider(LLMProvider):
    def __init__(self, model_name: str = "llama3"):
        self.client = ChatOllama(model=model_name)

    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
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
        
        # Ollama often runs locally
        response = await self.client.ainvoke(lc_messages)
        return response.content
