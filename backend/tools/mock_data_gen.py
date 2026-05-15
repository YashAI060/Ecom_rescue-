from faker import Faker
import sqlite3
import os
import random

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "vera.db")

def populate_mock_data():
    fake = Faker()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Clear existing data
    cursor.execute("DELETE FROM inventory")
    cursor.execute("DELETE FROM alerts")
    cursor.execute("DELETE FROM agent_logs")
    
    # Add some products
    products = [
        ("AeroStride Sneakers", "SKU-AERO-001", 5, 120.0),
        ("CloudWalk Sandals", "SKU-CLD-002", 0, 45.0),
        ("PeakPerformance Tee", "SKU-PK-003", 50, 30.0),
        ("HydroGuard Backpack", "SKU-HGD-004", 2, 85.0)
    ]
    
    for name, sku, stock, price in products:
        status = 'paused' if stock == 0 else 'active'
        cursor.execute(
            "INSERT INTO inventory (product_name, sku, stock_level, price, ad_status) VALUES (?, ?, ?, ?, ?)",
            (name, sku, stock, price, status)
        )
        
    # Add some initial alerts
    for _ in range(5):
        source = random.choice(['Twitter', 'Customer Email', 'Reddit'])
        sentiment = random.choice(['negative', 'neutral', 'positive'])
        content = fake.sentence()
        roi_impact = random.uniform(10.0, 150.0) if sentiment == 'negative' else 0.0
        cursor.execute(
            "INSERT INTO alerts (source, content, sentiment, roi_impact) VALUES (?, ?, ?, ?)",
            (source, content, sentiment, roi_impact)
        )

    conn.commit()
    conn.close()
    print("Mock data populated.")

if __name__ == "__main__":
    populate_mock_data()
