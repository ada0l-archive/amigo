from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import User
from amigo.functions.private.help import PrivateHelp


class PrivateStart(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["start", ], "func": cls.is_private}

    def main(self, message):
        user, was_created = ModelManager(self.db, User).create(
            allow_duplication=False,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )

        if was_created:
            self.bot.reply_to(message, 'Bot is started')
        else:
            self.bot.reply_to(message, 'Bot is already started')

        self.next(message, PrivateHelp)
