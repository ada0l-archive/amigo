from amigo.models import Chat, Participation, ParticipationStatus, ModelManager
from amigo.views.base import BaseView


class StatusView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["status", ]}

    def group(self, message):
        chat = ModelManager(self.db, Chat).get_object(
            filter={
                "telegram_id": message.chat.id
            })

        if not chat:
            self.bot.reply_to(message, "Chat is not started")
            return

        participants = ModelManager(self.db, Participation).get_objects(
            filter={
                "chat": chat
            })

        not_completed = ModelManager(self.db, Participation).get_objects(
            filter={
                "chat": chat,
                "hobby": "",
                "wishes": "",
                "not_wishes": "",
                "address": "",
            })

        self.bot.reply_to(
            message,
            "Chat is started.\n"
            "The number of filled forms: "
            f"{len(participants) - len(not_completed)}/{len(participants)}"
        )

    def private(self, message):
        self.bot.reply_to(message, "This command works only in groups")
