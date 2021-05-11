from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import Chat


class GroupStart(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["start", ], "func": cls.is_group}

    def main(self, message):
        chat, was_created = ModelManager(self.db, Chat).create(
            allow_duplication=False,
            telegram_id=message.chat.id,
            title=message.chat.title
        )

        if was_created:
            self.bot.reply_to(message, "Chat is started")
        else:
            self.bot.reply_to(message, "Chat already started")
