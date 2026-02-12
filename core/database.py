from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from core.settings import settings


class Database:
    client: Optional[AsyncIOMotorClient] = None
    
    @classmethod
    async def connect_db(cls):
        cls.client = AsyncIOMotorClient(settings.MONGODB_URL)
        print(f"Connected to MongoDB at {settings.MONGODB_URL}")
    
    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()
            print("Closed MongoDB connection")
    
    @classmethod
    def get_db(cls):
        if cls.client is None:
            raise Exception("Database not connected")
        return cls.client[settings.MONGODB_DB_NAME]


db = Database()
