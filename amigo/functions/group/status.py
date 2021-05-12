from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import Chat, Participation, ParticipationStatus


class GroupStatus(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["status", ], "func": cls.is_group}

    def main(self, message):
        chat = ModelManager(self.db, Chat).get_object(
            telegram_id=message.chat.id
        )
        if not chat:
            self.bot.reply_to(message, "Chat is not started")
            return

        participants = ModelManager(self.db, Participation).get_objects(
            chat=chat
        )

        completed = ModelManager(self.db, Participation).get_objects(
            chat=chat,
            status=ParticipationStatus.COMPLETE
        )

        self.bot.reply_to(
            message,
            "Chat is started.\n"
            "The number of filled forms: "
            f"{len(completed)}/{len(participants)}"
        )
