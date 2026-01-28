from app.models.message import Message

class IntentClassifier:
    async def classify(self, message: Message) -> str:
        # Placeholder logic
        text = message.content.lower()
        if "help" in text:
            return "support"
        elif "price" in text or "cost" in text:
            return "pricing"
        return "general"
