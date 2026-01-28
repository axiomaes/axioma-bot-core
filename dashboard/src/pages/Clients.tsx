import React, { useEffect, useState } from 'react';
import { getClients } from '../services/api';
import type { Client } from '../types';
import { Layers, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

const Clients: React.FC = () => {
    const [clients, setClients] = useState<Client[]>([]);

    useEffect(() => {
        getClients().then(setClients);
    }, []);

    return (
        <div>
            <h2 className="text-3xl font-bold mb-8">Clients & Workflows</h2>
            <div className="grid grid-cols-1 gap-4">
                {clients.map(client => (
                    <div key={client.id} className="bg-white/5 border border-white/10 p-6 rounded-lg flex md:flex-row flex-col items-center justify-between">
                        <div className="flex items-center gap-4 mb-4 md:mb-0">
                            <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center text-primary font-bold text-xl">
                                {client.name.charAt(0)}
                            </div>
                            <div>
                                <h3 className="text-xl font-bold">{client.name}</h3>
                                <div className="flex items-center gap-2 text-sm text-gray-400 mt-1">
                                    <Layers size={14} />
                                    <span>Workflow: {client.workflow}</span>
                                </div>
                            </div>
                        </div>

                        <div className="flex gap-3">
                            <Link
                                to={`/workflows/${client.id}`}
                                className="px-4 py-2 rounded bg-white/5 hover:bg-white/10 border border-white/10 flex items-center gap-2 transition-colors"
                            >
                                View Workflow <ArrowRight size={16} />
                            </Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Clients;
