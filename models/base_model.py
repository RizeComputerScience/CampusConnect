import sqlite3

class BaseModel:
    DB_PATH = "db/campusconnect.db"

    @classmethod
    def connect(cls):
        return sqlite3.connect(cls.DB_PATH)
