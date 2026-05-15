from database.queries import log_agent_action, add_alert

class ScoutAgent:
    """Agent 1: Ingestion & Sentiment Parsing"""
    def __init__(self):
        self.name = "SCOUT"

    def process_signal(self, source, content):
        log_agent_action(self.name, f"Ingesting signal from {source}", "PARSING")
        
        # Simple sentiment logic for demo
        sentiment = "neutral"
        if any(word in content.lower() for word in ["bad", "horrible", "broken", "out of stock", "wait"]):
            sentiment = "negative"
        elif any(word in content.lower() for word in ["great", "love", "awesome"]):
            sentiment = "positive"
            
        log_agent_action(self.name, f"Signal sentiment: {sentiment}", "CLASSIFIED")
        return {"source": source, "content": content, "sentiment": sentiment}
