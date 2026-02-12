from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from users.services import user_service

class TelegramService:
    def __init__(self, application):
        self.application = application

    def register_handlers(self):
        self.application.add_handler(CommandHandler("start", self._on_start))
        self.application.add_handler(MessageHandler(filters.TEXT, self._on_message))

    async def _on_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await user_service.UserService.create_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )
        await update.message.reply_text(f"سلام {user.first_name}! شما ثبت شدید.")

    async def _on_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        await user_service.process_user_message(update.effective_user.id, text)

    async def send_message(self, chat_id: int, text: str):
        return await self.application.bot.send_message(chat_id=chat_id, text=text)

    async def edit_message(self, chat_id: int, message_id: int, text: str):
        return await self.application.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)

    async def delete_message(self, chat_id: int, message_id: int):
        await self.application.bot.delete_message(chat_id=chat_id, message_id=message_id)
