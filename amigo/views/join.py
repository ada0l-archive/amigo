from amigo.models import Chat, ChatStatus, User, Participation, ModelManager
from amigo.views.base import BaseView


class JoinView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["join", ]}

    def group(self, message):
        chat = ModelManager(self.db, Chat).get_object(filter={
            "telegram_id": message.chat.id
        })

        if not chat:
            self.bot.reply_to(message, "Chat is not started")
            return

        if chat.status != ChatStatus.STARTED:
            self.bot.reply_to(
                message,
                "Something went wrong. Chat status is not correct for "
                "this action"
            )
            return

        user, _ = ModelManager(self.db, User).create(
            allow_duplication=False,
            args={
                "telegram_id": message.from_user.id,
                "username": message.from_user.username
            })

        part, was_created = ModelManager(self.db, Participation).create(
            allow_duplication=False,
            args={
                "user": user,
                "chat": chat
            }
        )

        if was_created:
            self.bot.reply_to(message, "You are joined")
        else:
            self.bot.reply_to(message, "You are already joined")

    def private(self, message):
        self.bot.reply_to(message, "This command works only in groups")
