from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Dict, Any
import operator
from app.models.message import Message

class AgentState(TypedDict):
    input_message: Message
    history: list
    context: Dict[str, Any]
    final_response: str

class BaseGraph:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        self._build_graph()
        self.compiled_app = self.workflow.compile()

    def _build_graph(self):
        # Define nodes
        self.workflow.add_node("classify", self.classify_node)
        self.workflow.add_node("process", self.process_node)
        self.workflow.add_node("generate", self.generate_node)

        # Define edges
        self.workflow.set_entry_point("classify")
        self.workflow.add_edge("classify", "process")
        self.workflow.add_edge("process", "generate")
        self.workflow.add_edge("generate", END)

    async def classify_node(self, state: AgentState):
        # Mock logic
        return {"context": {"intent": "general"}}

    async def process_node(self, state: AgentState):
        # Mock logic
        return {"context": {**state["context"], "processed": True}}

    async def generate_node(self, state: AgentState):
        return {"final_response": f"Echo: {state['input_message'].content}"}

    async def run(self, message: Message):
        initial_state = {
            "input_message": message,
            "history": [],
            "context": {},
            "final_response": ""
        }
        result = await self.compiled_app.ainvoke(initial_state)
        return result["final_response"]
