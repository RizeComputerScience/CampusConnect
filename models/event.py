from models.base_model import BaseModel

class Event(BaseModel):
    def __init__(self, event_id, title, location, date):
        self.event_id = event_id
        self.title = title
        self.location = location
        self.date = date
