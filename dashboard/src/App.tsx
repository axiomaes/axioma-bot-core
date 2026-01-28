import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Clients from './pages/Clients';
import WorkflowViewer from './pages/WorkflowViewer';
import ExecutionDetail from './pages/ExecutionDetail';
import Logs from './pages/Logs';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/clients" element={<Clients />} />
          <Route path="/workflows/:clientId" element={<WorkflowViewer />} />
          <Route path="/executions/:id" element={<ExecutionDetail />} />
          <Route path="/logs" element={<Logs />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
