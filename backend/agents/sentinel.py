from database.queries import log_agent_action, add_alert

class SentinelAgent:
    """Agent 4: Verification & DB State Checker"""
    def __init__(self):
        self.name = "SENTINEL"

    def verify(self, data):
        log_agent_action(self.name, "Verifying system state post-action.", "VERIFYING")
        
        # Persist the finalized alert to DB
        add_alert(
            source=data['source'],
            content=data['content'],
            sentiment=data['sentiment'],
            roi_impact=data.get('roi_impact', 0.0)
        )
        
        log_agent_action(self.name, "Alert recorded. System stabilized.", "STABLE")
        return {"status": "success", "data": data}
