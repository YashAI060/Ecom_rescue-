import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GlassCard from '../components/GlassCard';
import ROIBar from '../components/ROIBar';
import TypewriterTerminal from '../components/TypewriterTerminal';
import StatusIndicator from '../components/StatusIndicator';
import { Activity, Shield, AlertCircle } from 'lucide-react';

const MainDashboard = () => {
  const [stats, setStats] = useState({ roi_saved: 284, response_time: "8s", status: "Green" });
  const [logs, setLogs] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const statsRes = await axios.get('http://localhost:8000/dashboard/stats');
        const logsRes = await axios.get('http://localhost:8000/dashboard/logs');
        const alertsRes = await axios.get('http://localhost:8000/dashboard/alerts');
        
        setStats(statsRes.data);
        setLogs(logsRes.data);
        setAlerts(alertsRes.data);
      } catch (e) {
        console.error("Backend not reachable", e);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="max-w-md mx-auto p-6 space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold glow-text tracking-tighter">VERA</h1>
          <p className="text-[10px] text-dim uppercase tracking-[0.2em]">Ecomm Rescue OS</p>
        </div>
        <StatusIndicator status={stats.status} />
      </header>

      <ROIBar savedAmount={stats.roi_saved} responseTime={stats.response_time} />

      <GlassCard className="space-y-4">
        <div className="flex items-center gap-2 mb-2">
          <Activity size={16} className="text-primary" />
          <h2 className="text-sm font-bold uppercase tracking-wider">Live Agent Stream</h2>
        </div>
        <TypewriterTerminal logs={logs} />
      </GlassCard>

      <div className="grid grid-cols-1 gap-4">
        <div className="flex items-center gap-2 px-2">
          <AlertCircle size={16} className="text-error" />
          <h2 className="text-sm font-bold uppercase tracking-wider">Recent Rescues</h2>
        </div>
        {alerts.map((alert, i) => (
          <GlassCard key={i} className="py-4 flex justify-between items-center">
            <div>
              <p className="text-xs font-bold text-white/90">{alert.source}</p>
              <p className="text-[10px] text-dim truncate w-40">{alert.content}</p>
            </div>
            <div className="text-right">
              <p className={`text-xs font-bold ${alert.sentiment === 'negative' ? 'text-error' : 'text-success'}`}>
                {alert.sentiment}
              </p>
              <p className="text-[10px] text-white/40">Saved ${alert.roi_impact}</p>
            </div>
          </GlassCard>
        ))}
      </div>
      
      <div className="pt-4 flex justify-center opacity-30">
        <Shield size={40} className="text-primary" />
      </div>
    </div>
  );
};

export default MainDashboard;
