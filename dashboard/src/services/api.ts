import axios from 'axios';
import type { Execution, Client, Workflow } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
});

export const getExecutions = async () => {
    const response = await api.get<Execution[]>('/dashboard/executions');
    return response.data;
};

export const getExecution = async (id: string) => {
    const response = await api.get<Execution>(`/dashboard/executions/${id}`);
    return response.data;
};

export const getClients = async () => {
    const response = await api.get<Client[]>('/dashboard/clients');
    return response.data;
};

export const getWorkflow = async (clientId: string) => {
    const response = await api.get<Workflow>(`/dashboard/workflows/${clientId}`);
    return response.data;
};
