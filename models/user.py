from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, user_id, name, preferences):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences
