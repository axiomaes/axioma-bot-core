from abc import ABC, abstractmethod
from typing import Any, List, Dict

class LLMProvider(ABC):
    @abstractmethod
    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        pass
