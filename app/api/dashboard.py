from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from app.services.execution_store import ExecutionStore, get_execution_store
from app.graph.workflow_loader import WorkflowLoader
import os

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/executions")
async def get_executions(store: ExecutionStore = Depends(get_execution_store)):
    return store.get_executions()

@router.get("/executions/{execution_id}")
async def get_execution_detail(execution_id: str, store: ExecutionStore = Depends(get_execution_store)):
    exec_data = store.get_execution(execution_id)
    if not exec_data:
        raise HTTPException(status_code=404, detail="Execution not found")
    return exec_data

@router.get("/clients")
async def get_clients():
    # Mocked client list based on directory structure or config
    # In a real app, this would come from a DB
    workflows_dir = "app/workflows"
    clients = []
    
    if os.path.exists(workflows_dir):
        for name in os.listdir(workflows_dir):
            if os.path.isdir(os.path.join(workflows_dir, name)):
                clients.append({
                    "id": name,
                    "name": name.capitalize(),
                    "workflow": "default" if name == "default" else f"{name}_workflow"
                })
    return clients

@router.get("/workflows/{client_id}")
async def get_client_workflow(client_id: str):
    loader = WorkflowLoader()
    workflow = loader.load_workflow(client_id)
    if not workflow:
         raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow
