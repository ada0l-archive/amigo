from amigo.functions.base_functions import BaseFunction


class GroupHelp(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["help", ], "func": cls.is_group}

    def main(self, message):
        self.bot.reply_to(
            message,
            "Hi, I'm the bot that will help you organize your secret "
            "santa event.\n"
            "/start - launch bot in group\n"
            "/join - take part in the event\n"
        )
