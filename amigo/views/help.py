from amigo.views.base import BaseView


class HelpView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["help", ]}

    def group(self, message):
        self.bot.reply_to(
            message,
            "Hi, I'm the bot that will help you organize your secret "
            "santa event.\n"
            "/start - launch bot in group\n"
            "/join - take part in the event\n"
            "/help - show this message"
        )

    def private(self, message):
        self.bot.reply_to(
            message,
            "hello amigo\n"
            "/start - start bot in private chat\n"
            "/choose - select a group to edit\n"
            "/edit - fill in the data\n"
            "/help - show this message"
        )
