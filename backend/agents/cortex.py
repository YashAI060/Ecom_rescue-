from database.queries import log_agent_action

class CortexAgent:
    """Agent 2: Correlation, ROI Calc & Branching Logic"""
    def __init__(self):
        self.name = "CORTEX"

    def analyze(self, data):
        log_agent_action(self.name, f"Analyzing impact for sentiment: {data['sentiment']}", "CALCULATING")
        
        roi_impact = 0.0
        action_required = False
        
        if data['sentiment'] == "negative":
            # Mock ROI calculation: If people are complaining about stock, ads are wasting money
            roi_impact = 42.50 # Mock value per mention
            action_required = True
            log_agent_action(self.name, f"Identified potential loss: ${roi_impact}", "ROI_ALERT")
        
        data['roi_impact'] = roi_impact
        data['action_required'] = action_required
        return data
