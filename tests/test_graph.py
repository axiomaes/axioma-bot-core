import pytest
from app.graph.base_graph import BaseGraph
from app.models.message import Message

@pytest.mark.asyncio
async def test_base_graph_execution():
    graph = BaseGraph()
    message = Message(
        id="123",
        content="Hello world",
        sender_id="user1",
        conversation_id="conv1",
        inbox_id="1",
        account_id="1"
    )
    
    response = await graph.run(message)
    assert "Echo: Hello world" in response
