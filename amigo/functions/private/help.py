from amigo.functions.base_functions import BaseFunction


class PrivateHelp(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["help", ], "func": cls.is_private}

    def main(self, message):
        self.bot.reply_to(
            message,
            "hello amigo\n"
            "/start - start bot in private chat\n"
            "/choose - select a group to edit\n"
            "/edit - fill in the data\n"
        )