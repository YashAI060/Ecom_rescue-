import React, { useEffect, useRef } from 'react';

const TypewriterTerminal = ({ logs }) => {
  const terminalRef = useRef(null);

  useEffect(() => {
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight;
    }
  }, [logs]);

  return (
    <div ref={terminalRef} className="bg-black/40 rounded-xl p-4 font-mono text-[10px] h-48 overflow-y-auto border border-white/5">
      {logs.map((log, i) => (
        <div key={i} className="mb-1">
          <span className="text-secondary">[{log.timestamp.split('T')[1].split('.')[0]}]</span>{' '}
          <span className="text-primary font-bold">{log.agent_name}:</span>{' '}
          <span className="text-white/80">{log.message}</span>{' '}
          {log.action_taken && (
            <span className="bg-white/10 px-1 rounded text-[8px] text-primary">{log.action_taken}</span>
          )}
        </div>
      ))}
      {logs.length === 0 && <div className="text-dim">Waiting for agent activity...</div>}
    </div>
  );
};

export default TypewriterTerminal;
