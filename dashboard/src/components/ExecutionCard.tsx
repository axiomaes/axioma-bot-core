import React from 'react';
import type { Execution } from '../types';
import { Link } from 'react-router-dom';
import { Activity, Clock } from 'lucide-react';
import { clsx } from 'clsx';

interface ExecutionCardProps {
    execution: Execution;
}

const ExecutionCard: React.FC<ExecutionCardProps> = ({ execution }) => {
    const isCompleted = execution.status === 'completed';
    const isError = execution.steps.some(s => s.error);

    return (
        <Link
            to={`/executions/${execution.execution_id}`}
            className="block bg-white/5 border border-white/10 rounded-lg p-5 hover:bg-white/10 transition-colors"
        >
            <div className="flex justify-between items-start mb-3">
                <div>
                    <h3 className="font-semibold text-lg text-white">{execution.workflow_name}</h3>
                    <p className="text-sm text-gray-400">Client: <span className='text-secondary'>{execution.client_id}</span></p>
                </div>
                <div className={clsx(
                    "px-2 py-1 rounded text-xs font-bold uppercase",
                    isError ? "bg-red-500/20 text-red-400" : (isCompleted ? "bg-green-500/20 text-green-400" : "bg-blue-500/20 text-blue-400")
                )}>
                    {isError ? "Error" : execution.status}
                </div>
            </div>

            <div className="grid grid-cols-2 gap-4 text-sm text-gray-400 mb-4">
                <div className="flex items-center gap-2">
                    <Clock size={16} />
                    <span>{new Date(execution.timestamp).toLocaleTimeString()}</span>
                </div>
                <div className="flex items-center gap-2">
                    <Activity size={16} />
                    <span>{execution.steps.length} steps</span>
                </div>
            </div>

            <div className="border-t border-white/10 pt-3 flex items-center justify-between text-xs">
                <span className="text-gray-500 truncate max-w-[200px]">{execution.input_message}</span>
                <span className="text-primary hover:underline">View details &rarr;</span>
            </div>
        </Link>
    );
};

export default ExecutionCard;
