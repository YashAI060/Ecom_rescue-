import React from 'react';
import { TrendingUp, Clock } from 'lucide-react';

const ROIBar = ({ savedAmount, responseTime }) => {
  return (
    <div className="glass-card flex justify-between items-center px-6 py-3 mb-4">
      <div className="flex items-center gap-2">
        <TrendingUp size={18} className="text-primary" />
        <span className="text-sm font-medium">
          <span className="text-primary font-bold">${savedAmount}</span> saved
        </span>
      </div>
      <div className="h-4 w-[1px] bg-white/10" />
      <div className="flex items-center gap-2">
        <Clock size={18} className="text-secondary" />
        <span className="text-sm font-medium">
          <span className="text-secondary font-bold">{responseTime}</span> response
        </span>
      </div>
    </div>
  );
};

export default ROIBar;
