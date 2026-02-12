from typing import Optional
from telegram.ext import Application, ApplicationBuilder

from core.settings import settings


class TelegramDriver:
    application: Optional[Application] = None
    handler: Optional["TelegramService"] = None
    
    @classmethod
    async def connect(cls):
        if not settings.TELEGRAM_BOT_TOKEN:
            print("Telegram bot token not configured")
            return

        cls.application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
        await cls.application.initialize()
        await cls.application.start()
        if cls.application.updater:
            await cls.application.updater.start_polling()

        from telegram_app.services import telegram_service
        cls.handler = telegram_service.TelegramService(cls.application)
        print("Connected to Telegram")
    
    @classmethod
    async def disconnect(cls):
        if cls.application:
            if cls.application.updater:
                await cls.application.updater.stop()
            await cls.application.stop()
            await cls.application.shutdown()
            print("Disconnected from Telegram")
    
    @classmethod
    def get_handler(cls):
        return cls.handler


telegram = TelegramDriver()
