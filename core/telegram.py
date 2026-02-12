from typing import Optional
import asyncio
import logging

from telegram.error import NetworkError
from telegram.ext import Application, ApplicationBuilder

from core.settings import settings


class TelegramDriver:
    application: Optional[Application] = None
    handler: Optional["TelegramService"] = None
    logger = logging.getLogger("aury.telegram")

    @classmethod
    async def connect(cls):
        if not settings.TELEGRAM_BOT_TOKEN:
            cls.logger.warning("Telegram bot token not configured")
            return

        cls.application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        from telegram_app.services import telegram_service
        cls.handler = telegram_service.TelegramService(cls.application)
        cls.handler.register_handlers()

        max_attempts = 5
        base_delay = 2
        for attempt in range(1, max_attempts + 1):
            try:
                await cls.application.initialize()
                await cls.application.start()
                if cls.application.updater:
                    await cls.application.updater.start_polling()
                cls.logger.info("Connected to Telegram (polling started)")
                return
            except NetworkError as exc:
                cls.logger.warning(
                    "Telegram network error during startup (attempt %s/%s): %s",
                    attempt,
                    max_attempts,
                    exc,
                )
                if attempt == max_attempts:
                    break
                await asyncio.sleep(base_delay * attempt)

        cls.logger.error("Telegram polling not started after %s attempts", max_attempts)
        cls.handler = None
        if cls.application:
            await cls.application.shutdown()
            cls.application = None
        return

    @classmethod
    async def disconnect(cls):
        if not cls.application:
            return

        if cls.application.updater:
            await cls.application.updater.stop()
        await cls.application.stop()
        await cls.application.shutdown()
        cls.logger.info("Disconnected from Telegram")

    @classmethod
    def get_handler(cls):
        return cls.handler


telegram = TelegramDriver()
