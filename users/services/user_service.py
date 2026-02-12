from datetime import datetime
import logging
from typing import Any

from users.models import User

logger = logging.getLogger("aury.users")


class UserService:

    @staticmethod
    async def create_user(user_id: Any, username: str | None, first_name: str | None, last_name: str | None):
        exists = User.find(User.telegram_id == user_id)
        if exists:
            return True
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
        await user.insert()
        logger.info("user saved=%s", user_id)

        return False


async def process_user_message(user_id: Any, text: str) -> None:
    """Placeholder for processing incoming messages."""
    _ = user_id, text
