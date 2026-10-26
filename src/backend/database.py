import sqlite3
import os

DB_PATH = os.path.join("data", "sentinel_history.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS execution_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT,
            total_tests INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_execution(status: str, total_tests: int):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO execution_history (status, total_tests) VALUES (?, ?)", (status, total_tests))
    conn.commit()
    conn.close()