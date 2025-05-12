import os
from flask import Blueprint, render_template
import sqlite3
event_bp = Blueprint('event', __name__)
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db', 'campusconnect.db')
DB_PATH = os.path.abspath(DB_PATH)  # Ensures full absolute path

@event_bp.route("/events")
def events():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Fetch internal events - Example
    cursor.execute("SELECT title, location, date FROM events")
    internal_events = cursor.fetchall()
    # Print out values for debugging
    print(internal_events)

    # Fetch external events 
    # Update the extenal_events variable with the data you want to display
    external_events = []

    conn.close()
    return render_template("events.html", internal_events=internal_events, external_events=external_events)