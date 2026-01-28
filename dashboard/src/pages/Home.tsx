import React, { useEffect, useState } from 'react';
import { getExecutions, getClients } from '../services/api';
import type { Execution, Client } from '../types';
import ExecutionCard from '../components/ExecutionCard';
import { Activity, Users, Layers, Zap } from 'lucide-react';

const Home: React.FC = () => {
    const [executions, setExecutions] = useState<Execution[]>([]);
    const [clients, setClients] = useState<Client[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchData() {
            try {
                const [execData, clientData] = await Promise.all([getExecutions(), getClients()]);
                setExecutions(execData);
                setClients(clientData);
            } catch (e) {
                console.error("Failed to fetch data", e);
            } finally {
                setLoading(false);
            }
        }
        fetchData();
    }, []);

    const stats = [
        { label: 'Total Clients', value: clients.length, icon: Users, color: 'text-blue-400' },
        { label: 'Active Workflows', value: clients.length, icon: Layers, color: 'text-purple-400' }, // Approximation
        { label: 'Recent Executions', value: executions.length, icon: Activity, color: 'text-green-400' },
        { label: 'Success Rate', value: '100%', icon: Zap, color: 'text-yellow-400' }, // Mock
    ];

    return (
        <div>
            <div className="mb-8">
                <h2 className="text-3xl font-bold mb-2">Dashboard Overview</h2>
                <p className="text-gray-400">Real-time insights into Axioma Bot Core</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
                {stats.map((stat, i) => {
                    const Icon = stat.icon;
                    return (
                        <div key={i} className="bg-white/5 border border-white/10 p-6 rounded-lg">
                            <div className="flex items-center justify-between mb-4">
                                <div className={`p-2 rounded bg-white/5 ${stat.color}`}>
                                    <Icon size={24} />
                                </div>
                                <span className="text-2xl font-bold">{stat.value}</span>
                            </div>
                            <div className="text-sm text-gray-400">{stat.label}</div>
                        </div>
                    );
                })}
            </div>

            <h3 className="text-xl font-bold mb-4">Recent Executions</h3>
            {loading ? (
                <div className="text-center py-10">Loading...</div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {executions.length === 0 ? (
                        <div className="col-span-3 text-gray-500 text-center py-10">No recent executions found.</div>
                    ) : (
                        executions.map(ex => <ExecutionCard key={ex.execution_id} execution={ex} />)
                    )}
                </div>
            )}
        </div>
    );
};

export default Home;
