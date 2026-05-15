import React from 'react';

const StatusIndicator = ({ status = 'Green' }) => {
  const isHealthy = status === 'Green';
  return (
    <div className="flex items-center gap-3">
      <div className={`h-3 w-3 rounded-full ${isHealthy ? 'bg-success' : 'bg-error'} pulse`} 
           style={{ boxShadow: `0 0 10px ${isHealthy ? 'var(--success)' : 'var(--error)'}` }} />
      <span className={`text-xs font-bold uppercase tracking-widest ${isHealthy ? 'text-success' : 'text-error'}`}>
        System {status}
      </span>
    </div>
  );
};

export default StatusIndicator;
