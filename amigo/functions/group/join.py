from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import Chat, ChatStatus, User, Participation


class GroupJoin(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["join", ], "func": cls.is_group}

    def main(self, message):
        chat = ModelManager(self.db, Chat).get_object(
            telegram_id=message.chat.id
        )
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

        user = ModelManager(self.db, User).get_object(
            telegram_id=message.from_user.id
        )

        if not user:
            self.bot.reply_to(message, "You are not start me in private chat")
            return

        part, was_created = ModelManager(self.db, Participation).create(
            allow_duplication=False,
            user=user,
            chat=chat
        )

        if was_created:
            self.bot.reply_to(message, "You are joined")
        else:
            self.bot.reply_to(message, "You are already joined")
