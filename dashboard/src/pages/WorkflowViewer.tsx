import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getWorkflow } from '../services/api';
import type { Workflow } from '../types';

const WorkflowViewer: React.FC = () => {
    const { clientId } = useParams<{ clientId: string }>();
    const [workflow, setWorkflow] = useState<Workflow | null>(null);

    useEffect(() => {
        if (clientId) {
            getWorkflow(clientId).then(setWorkflow);
        }
    }, [clientId]);

    if (!workflow) return <div>Loading...</div>;

    return (
        <div>
            <h2 className="text-3xl font-bold mb-6">Workflow: {workflow.name || clientId}</h2>
            <div className="bg-white/5 p-6 rounded-lg border border-white/10 font-mono text-sm whitespace-pre-wrap">
                {JSON.stringify(workflow, null, 2)}
            </div>

            {/* Visualizer Placeholder */}
            <div className="mt-8 p-10 border-2 border-dashed border-white/10 rounded-lg text-center text-gray-500">
                Graph visualization would be rendered here.
            </div>
        </div>
    );
};

export default WorkflowViewer;
