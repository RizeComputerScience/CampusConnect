
from flask import Blueprint, render_template

event_bp = Blueprint('event', __name__)

# Starter code
# @event_bp.route("/events")
# def events():
#     return render_template("events.html")
# End Starter Code

# Updated final code
import sqlite3
@event_bp.route("/events")
def events():
    conn = sqlite3.connect("db/campusconnect.db")
    cursor = conn.cursor()
    # Fetch internal events
    cursor.execute("SELECT title, location, date FROM events")
    internal = cursor.fetchall()
    print(internal)

    # Fetch external (scraped) events
    cursor.execute("SELECT title, location, date, description FROM external_events")
    external = cursor.fetchall()
    print(external)

    conn.close()

    return render_template("events.html", internal_events=internal, external_events=external)
