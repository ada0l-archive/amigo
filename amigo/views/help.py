from amigo.views.base import BaseView


class HelpView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["help", ]}

    def group(self, message):
        self.bot.reply_to(
            message,
            "Hi, I'm Amigo and I will help you organize your secret "
            "santa event.\n"
            " - Write /start to create an event.\n"
            " - If you want to join the event, then write /join.\n"
            f" - To fill form for this group, write /join and {self.get_link_to_me('write to me')} "
            "in private messages.\n"
            " - To send forms to members, write /send.",
            parse_mode="HTML"
        )

    def private(self, message):
        self.bot.reply_to(
            message,
            "hello amigo\n"
            " - Write /edit to fill in the data for any chat"
        )
