from agents.scout import ScoutAgent
from agents.cortex import CortexAgent
from agents.shield import ShieldAgent
from agents.sentinel import SentinelAgent

class VeraWorkflow:
    def __init__(self):
        self.scout = ScoutAgent()
        self.cortex = CortexAgent()
        self.shield = ShieldAgent()
        self.sentinel = SentinelAgent()

    def run(self, source, content):
        # Sequential DAG execution
        res1 = self.scout.process_signal(source, content)
        res2 = self.cortex.analyze(res1)
        res3 = self.shield.execute(res2)
        final = self.sentinel.verify(res3)
        return final
