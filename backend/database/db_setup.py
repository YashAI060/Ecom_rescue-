import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "vera.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Inventory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            sku TEXT UNIQUE NOT NULL,
            stock_level INTEGER DEFAULT 0,
            price REAL,
            ad_status TEXT DEFAULT 'active' -- 'active' or 'paused'
        )
    ''')
    
    # Sentiment/Alerts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            source TEXT, -- 'twitter', 'email', 'support'
            content TEXT,
            sentiment TEXT, -- 'positive', 'neutral', 'negative'
            roi_impact REAL DEFAULT 0.0,
            status TEXT DEFAULT 'pending' -- 'pending', 'resolved'
        )
    ''')
    
    # Agent logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agent_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            agent_name TEXT,
            message TEXT,
            action_taken TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

if __name__ == "__main__":
    init_db()
