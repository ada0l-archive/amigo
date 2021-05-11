from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import Chat


class GroupStop(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["stop", ], "func": cls.is_group}

    def main(self, message):
        chat, was_deleted = ModelManager(self.db, Chat).delete(
            telegram_id=message.chat.id,
        )

        if was_deleted:
            self.bot.reply_to(message, "Chat is stopped")
        else:
            self.bot.reply_to(
                message,
                "Something went wrong. Maybe the bot wasn't started"
            )
