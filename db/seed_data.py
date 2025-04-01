import sqlite3
import os

DB_PATH = "db/campusconnect.db"

# Remove existing DB for a clean seed (optional in dev environment)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create tables manually or run schema.sql separately if preferred
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    preferences TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    location TEXT,
    date TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS external_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    date TEXT,
    location TEXT,
    description TEXT
)''')

# Users
c.execute("INSERT INTO events (title, location, date) VALUES (?, ?, ?)", ("Music Night", "Student Center", "2025-04-05"))

# Internal events
c.execute("INSERT INTO events (title, location, date) VALUES (?, ?, ?)", ("Hackathon", "Library", "2025-04-01"))

conn.commit()
conn.close()