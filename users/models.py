from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import ConfigDict, Field


class User(Document):
    telegram_id: int = Field(..., description="Telegram user ID")
    username: Optional[str] = Field(None, description="Telegram username")
    first_name: Optional[str] = Field(None, description="First name")
    last_name: Optional[str] = Field(None, description="Last name")
    phone: Optional[str] = Field(None, description="Phone number")
    is_active: bool = Field(default=True, description="Is user active")
    is_blocked: bool = Field(default=False, description="Is user blocked")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_interaction: Optional[datetime] = Field(None, description="Last interaction with bot")
    
    class Settings:
        name = "users"

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "telegram_id": 123456789,
                "username": "john_doe",
                "first_name": "John",
                "last_name": "Doe",
                "is_active": True
            }
        }
    )
