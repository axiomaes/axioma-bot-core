import json
import os
from typing import Dict, Any

class WorkflowLoader:
    def __init__(self, workflows_dir: str = "app/workflows"):
        self.workflows_dir = workflows_dir

    def load_workflow(self, client_id: str) -> Dict[str, Any]:
        path = os.path.join(self.workflows_dir, client_id, "workflow.json")
        if not os.path.exists(path):
            # Fallback to default
            path = os.path.join(self.workflows_dir, "default", "workflow.json")
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            return {}
