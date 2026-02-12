from datetime import datetime
from typing import Any

from users.models import User


class UserService:

    @staticmethod
    async def create_user(user_id: Any, username: str | None, first_name: str | None, last_name: str | None):
        user = User(
            telegram_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_blocked=False,
            phone=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            last_interaction=datetime.now(),
        )
        await user.create()