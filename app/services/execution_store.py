from datetime import datetime
from typing import Dict, List, Any, Optional
import uuid
from collections import deque

class ExecutionStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ExecutionStore, cls).__new__(cls)
            cls._instance.executions = deque(maxlen=200)
            cls._instance.executions_by_id = {}
        return cls._instance

    def add_execution(self, 
                      client_id: str, 
                      workflow_name: str, 
                      input_message: str,
                      execution_id: Optional[str] = None) -> str:
        
        exec_id = execution_id or str(uuid.uuid4())
        record = {
            "execution_id": exec_id,
            "client_id": client_id,
            "workflow_name": workflow_name,
            "input_message": input_message,
            "output_message": None,
            "steps": [],
            "timestamp": datetime.now().isoformat(),
            "status": "running"
        }
        
        self.executions.appendleft(record)
        self.executions_by_id[exec_id] = record
        
        # Cleanup old id references if deque rotated
        if len(self.executions_by_id) > 200:
            # Rebuild dict matching deque (simple way to ensure consistency)
            self.executions_by_id = {ex["execution_id"]: ex for ex in self.executions}
            
        return exec_id

    def update_execution(self, execution_id: str, output_message: str, steps: List[Dict[str, Any]]):
        if execution_id in self.executions_by_id:
            record = self.executions_by_id[execution_id]
            record["output_message"] = output_message
            record["steps"] = steps
            record["status"] = "completed"

    def get_executions(self, limit: int = 50) -> List[Dict[str, Any]]:
        return list(self.executions)[:limit]

    def get_execution(self, execution_id: str) -> Optional[Dict[str, Any]]:
        return self.executions_by_id.get(execution_id)

_store = ExecutionStore()

def get_execution_store():
    return _store
