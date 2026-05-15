from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph.workflow import VeraWorkflow
from database.queries import get_recent_alerts, get_roi_stats, get_db_connection
import sqlite3
import os

app = FastAPI(title="Vera Ecomm Rescue API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = VeraWorkflow()

class Signal(BaseModel):
    source: str
    content: str

@app.get("/status")
def read_root():
    return {"status": "Vera is online", "agents": ["SCOUT", "CORTEX", "SHIELD", "SENTINEL"]}

@app.post("/process")
def process_signal(signal: Signal):
    result = workflow.run(signal.source, signal.content)
    return result

@app.get("/dashboard/stats")
def get_stats():
    roi = get_roi_stats()
    return {
        "roi_saved": roi,
        "response_time": "8s", # Mocked
        "status": "Green"
    }

@app.get("/dashboard/logs")
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agent_logs ORDER BY timestamp DESC LIMIT 20")
    logs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return logs

@app.get("/dashboard/alerts")
def get_alerts():
    return get_recent_alerts()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
