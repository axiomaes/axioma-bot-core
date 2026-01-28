import React, { type ReactNode } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Users, FileText, Menu } from 'lucide-react';
import { clsx } from 'clsx';

interface LayoutProps {
    children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
    const location = useLocation();

    const navItems = [
        { name: 'Home', path: '/', icon: LayoutDashboard },
        { name: 'Clients', path: '/clients', icon: Users },
        { name: 'Logs', path: '/logs', icon: FileText },
    ];

    return (
        <div className="min-h-screen flex bg-background text-light">
            {/* Sidebar */}
            <aside className="w-64 bg-black/20 border-r border-white/10 hidden md:flex flex-col">
                <div className="p-6">
                    <h1 className="text-2xl font-bold text-primary tracking-tight">Axioma Bot</h1>
                    <p className="text-sm text-gray-400">Core Dashboard</p>
                </div>

                <nav className="flex-1 px-4 space-y-2">
                    {navItems.map((item) => {
                        const Icon = item.icon;
                        const isActive = location.pathname === item.path;

                        return (
                            <Link
                                key={item.path}
                                to={item.path}
                                className={clsx(
                                    "flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors",
                                    isActive
                                        ? "bg-primary/20 text-primary border border-primary/20"
                                        : "text-gray-400 hover:bg-white/5 hover:text-white"
                                )}
                            >
                                <Icon size={20} />
                                <span className="font-medium">{item.name}</span>
                            </Link>
                        );
                    })}
                </nav>

                <div className="p-4 border-t border-white/10 text-xs text-gray-500 text-center">
                    v1.0.0
                </div>
            </aside>

            {/* Mobile Header (visible on small screens) */}
            <header className="md:hidden fixed top-0 w-full z-10 bg-background border-b border-white/10 p-4 flex items-center justify-between">
                <h1 className="text-xl font-bold text-primary">Axioma</h1>
                <Menu className="text-white" />
            </header>

            {/* Main Content */}
            <main className="flex-1 p-8 overflow-auto md:pt-8 pt-20">
                <div className="max-w-6xl mx-auto">
                    {children}
                </div>
            </main>
        </div>
    );
};

export default Layout;
