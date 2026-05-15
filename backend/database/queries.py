import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "vera.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def add_alert(source, content, sentiment, roi_impact=0.0):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alerts (source, content, sentiment, roi_impact) VALUES (?, ?, ?, ?)",
        (source, content, sentiment, roi_impact)
    )
    conn.commit()
    conn.close()

def log_agent_action(agent_name, message, action_taken=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO agent_logs (agent_name, message, action_taken) VALUES (?, ?, ?)",
        (agent_name, message, action_taken)
    )
    conn.commit()
    conn.close()

def update_inventory_status(sku, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE inventory SET ad_status = ? WHERE sku = ?",
        (status, sku)
    )
    conn.commit()
    conn.close()

def get_recent_alerts(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_roi_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(roi_impact) as total_saved FROM alerts")
    result = cursor.fetchone()
    conn.close()
    return result['total_saved'] or 0.0
