from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Dict, Any
import operator
from datetime import datetime
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
        
        # In a real LangGraph, we would inspect the event stream
        # For this prototype, we'll manually simulate a trace since we are mocking node execution in the single ainvoke call for now
        # OR we improve ainvoke to return state and we infer steps.
        
        # Let's assume standard ainvoke returns the final state
        result = await self.compiled_app.ainvoke(initial_state)
        
        # Manually constructing trace for this scaffold because actual LangGraph streaming is more complex
        # and we want to fit the requested trace format.
        steps = [
            {"node": "classify", "timestamp": datetime.now().isoformat(), "details": "Intent classified as general"},
            {"node": "process", "timestamp": datetime.now().isoformat(), "details": "Processed message"},
            {"node": "generate", "timestamp": datetime.now().isoformat(), "details": "Generated response"}
        ]
        
        return result["final_response"], steps
