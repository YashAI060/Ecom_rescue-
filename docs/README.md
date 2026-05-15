# VERA: Ecomm Rescue OS

VERA is a multi-agentic system powered by Google ADK 2.0 (Simulated) designed to automatically detect and mitigate e-commerce disasters (like stockouts with active ads) in real-time.

## Architecture

- **SCOUT (Agent 1):** Ingests social signals and support tickets, parsing sentiment.
- **CORTEX (Agent 2):** Correlates signals with inventory and calculates ROI impact/potential loss.
- **SHIELD (Agent 3):** Executes defensive tools (pausing ads, notifying customers).
- **SENTINEL (Agent 4):** Verifies the system state and logs the rescue event.

## Tech Stack

- **Backend:** FastAPI, SQLite3, Faker
- **Frontend:** React, Framer Motion, Lucide (Mobile Dashboard View)
- **Engine:** Google ADK 2.0 Logic

## Setup

1. **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python database/db_setup.py
   python tools/mock_data_gen.py
   python main.py
   ```

2. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
