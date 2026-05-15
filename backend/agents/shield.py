from database.queries import log_agent_action, update_inventory_status
from tools.inventory_api import pause_ads
from tools.communication_api import send_apology_dm

class ShieldAgent:
    """Agent 3: Action Execution (Tool Caller)"""
    def __init__(self):
        self.name = "SHIELD"

    def execute(self, data):
        if not data.get('action_required'):
            log_agent_action(self.name, "No critical action required.", "STANDBY")
            return data

        log_agent_action(self.name, "Executing defensive actions...", "EXECUTING")
        
        # Call mock tools
        pause_ads("SKU-CLD-002") # Mock SKU for demo
        send_apology_dm(data['source'], "We're on it! Our automated systems have paused ads for out-of-stock items.")
        
        log_agent_action(self.name, "Ads paused. Apology sent.", "COMPLETED")
        return data
