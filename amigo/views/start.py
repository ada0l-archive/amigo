from amigo.models import Chat, ModelManager, User
from amigo.views.base import BaseView


class StartView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["start", ]}

    def group(self, message):
        chat, was_created = ModelManager(self.db, Chat).create(
            allow_duplication=False,
            args={
                "telegram_id": message.chat.id
            }
        )

        if was_created:
            self.bot.reply_to(message, "Chat is started")
        else:
            self.bot.reply_to(message, "Chat already started")

    def private(self, message):
        user, was_created = ModelManager(self.db, User).create(
            allow_duplication=False,
            args={
                "telegram_id": message.from_user.id,
                "username": message.from_user.username
            })

        if was_created:
            self.bot.reply_to(message, 'Bot is started')
        else:
            self.bot.reply_to(message, 'Bot is already started')
