from amigo.models import Chat, ModelManager, User
from amigo.views.base import BaseView


class StopView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["stop", ]}

    def group(self, message):
        was_deleted = ModelManager(self.db, Chat).delete(
            filter={
                "telegram_id": message.chat.id
            })

        if was_deleted:
            self.bot.reply_to(message, "Bot is stopped")
        else:
            self.bot.reply_to(
                message,
                "Something went wrong. Maybe the bot wasn't started"
            )

    def private(self, message):
        was_deleted = ModelManager(self.db, User).delete(
            filter={
                "telegram_id": message.chat.id
            })

        if was_deleted:
            self.bot.reply_to(message, "Bot is stopped")
        else:
            self.bot.reply_to(
                message,
                "Something went wrong. Maybe the bot wasn't started"
            )