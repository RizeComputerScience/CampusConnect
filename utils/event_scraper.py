import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

class CampusEventScraper:
    def __init__(self, url, db_path="db/campusconnect.db"):
        self.url = url
        self.db_path = db_path

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching HTML: {e}")
            return None

    def parse_events(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        events = []
        # Example scraping logic for Adrian College events page
        for item in soup.select("div.content"):
            title_tag = item.select_one("p.title")
            date_tag = item.select_one("p.date")

            title = title_tag.get_text(strip=True) if title_tag else "Untitled Event"
            date = date_tag.get_text(strip=True) if date_tag else "Unknown Date"
            location = "TBD"  # Adrian site doesn't list location directly
            description = ""   # No description field present in provided block

            events.append({
                "title": title,
                "date": date,
                "location": location,
                "description": description
            })

        return events

    def save_events(self, events):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS external_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT,
            location TEXT,
            description TEXT
        )''')

        for event in events:
            cursor.execute('''INSERT INTO external_events (title, date, location, description)
                              VALUES (?, ?, ?, ?)''',
                           (event['title'], event['date'], event['location'], event['description']))

        conn.commit()
        conn.close()

    def filter_events_by_preferences(self, preferences):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT title, date, location, description FROM external_events")
        all_events = cursor.fetchall()
        conn.close()

        keywords = [kw.strip().lower() for kw in preferences.split(",")]
        matched_events = []

        for event in all_events:
            title, date, location, description = event
            if any(kw in title.lower() or kw in description.lower() for kw in keywords):
                matched_events.append({
                    "title": title,
                    "date": date,
                    "location": location,
                    "description": description
                })

        return matched_events

    def run(self, filter_for_user=False, user_preferences=""):
        html = self.fetch_html()
        if html:
            events = self.parse_events(html)
            self.save_events(events)
            print(f"{len(events)} events saved to the database.")

            if filter_for_user and user_preferences:
                matches = self.filter_events_by_preferences(user_preferences)
                print("\nRecommended Events Based on Your Interests:")
                for event in matches:
                    print(f"- {event['title']} on {event['date']} at {event['location']}")
    
# Example usage
if __name__ == "__main__":
    scraper = CampusEventScraper("https://www.adrian.edu/calendar")
    scraper.run(filter_for_user=True, user_preferences="last day")
