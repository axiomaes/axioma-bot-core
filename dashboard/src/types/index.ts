export interface ExecutionStep {
    node: string;
    timestamp: string;
    details?: string;
    error?: string;
}

export interface Execution {
    execution_id: string;
    client_id: string;
    workflow_name: string;
    input_message: string;
    output_message?: string;
    steps: ExecutionStep[];
    timestamp: string;
    status: "running" | "completed" | "error";
}

export interface Client {
    id: string;
    name: string;
    workflow: string;
}

export interface WorkflowStep {
    id: string;
    type: string;
    prompt?: string;
}

export interface Workflow {
    name: string;
    steps: WorkflowStep[];
}
