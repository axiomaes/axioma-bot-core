import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getExecution } from '../services/api';
import type { Execution } from '../types';
import { Clock, AlertTriangle, MessageSquare, Terminal } from 'lucide-react';
import { clsx } from 'clsx';

const ExecutionDetail: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [execution, setExecution] = useState<Execution | null>(null);

    useEffect(() => {
        if (id) {
            getExecution(id).then(setExecution);
        }
    }, [id]);

    if (!execution) return <div className="p-10 text-center">Loading execution details...</div>;

    return (
        <div>
            <div className="mb-8 border-b border-white/10 pb-6">
                <div className="flex items-center gap-3 mb-2">
                    <h2 className="text-3xl font-bold">Execution Detail</h2>
                    <span className="text-gray-500 font-mono text-sm bg-white/5 px-2 py-1 rounded">#{execution.execution_id.slice(0, 8)}</span>
                </div>
                <div className="flex gap-6 text-sm text-gray-400">
                    <span className="flex items-center gap-2"><Clock size={16} /> {new Date(execution.timestamp).toLocaleString()}</span>
                    <span className="flex items-center gap-2 text-secondary font-bold">Client: {execution.client_id}</span>
                    <span className={clsx(
                        "font-bold uppercase",
                        execution.status === 'completed' ? "text-green-400" : "text-blue-400"
                    )}>{execution.status}</span>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Left Column: Chat IO */}
                <div className="space-y-6">
                    <div className="bg-white/5 border border-white/10 rounded-lg p-5">
                        <h3 className="flex items-center gap-2 text-lg font-bold mb-4 text-blue-300">
                            <MessageSquare size={18} /> User Input
                        </h3>
                        <div className="bg-black/30 p-4 rounded text-gray-300 whitespace-pre-wrap">
                            {execution.input_message}
                        </div>
                    </div>

                    <div className="bg-white/5 border border-white/10 rounded-lg p-5">
                        <h3 className="flex items-center gap-2 text-lg font-bold mb-4 text-green-300">
                            <MessageSquare size={18} /> Agent Output
                        </h3>
                        <div className="bg-black/30 p-4 rounded text-gray-300 whitespace-pre-wrap">
                            {execution.output_message || "No output yet..."}
                        </div>
                    </div>
                </div>

                {/* Right Column: Steps Trace */}
                <div className="lg:col-span-2">
                    <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                        <Terminal size={20} /> Execution Trace
                    </h3>

                    <div className="space-y-4">
                        {execution.steps.map((step, idx) => (
                            <div key={idx} className="bg-white/5 border border-white/10 rounded-lg p-4 relative overflow-hidden">
                                <div className="absolute top-0 left-0 w-1 h-full bg-primary/50"></div>
                                <div className="flex justify-between items-start mb-2 pl-3">
                                    <span className="font-mono font-bold text-accent text-lg">{step.node}</span>
                                    <span className="text-xs text-gray-500">{new Date(step.timestamp).toLocaleTimeString()}</span>
                                </div>

                                {step.details && (
                                    <div className="pl-3 text-gray-400 text-sm">{step.details}</div>
                                )}

                                {step.error && (
                                    <div className="pl-3 mt-2 text-red-400 flex items-center gap-2">
                                        <AlertTriangle size={16} /> {step.error}
                                    </div>
                                )}
                            </div>
                        ))}

                        {execution.steps.length === 0 && (
                            <div className="text-center text-gray-500 py-10 bg-white/5 rounded-lg border-2 border-dashed border-white/10">
                                No steps recorded for this execution.
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ExecutionDetail;
