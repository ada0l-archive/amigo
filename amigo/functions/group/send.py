import random

from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager, ChatManager
from amigo.models import Chat, Participation, ParticipationStatus, ChatStatus


class GroupSend(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["send", ], "func": cls.is_group}

    def main(self, message):
        chat = ModelManager(self.db, Chat).get_object(
            telegram_id=message.chat.id
        )
        if not chat:
            self.bot.reply_to(message, "You dont started bot")
            return

        participants = ModelManager(self.db, Participation).get_objects(
            chat=chat
        )

        if len(participants) < 2:
            self.bot.reply_to(message, "There aren't enough participants")
            return

        all_complete = True
        for participant in participants:
            if participant.status != ParticipationStatus.COMPLETE:
                all_complete = False
                self.bot.send_message(
                    participant.user.telegram_id,
                    "you didn't fill in the fields for the "
                    f"{participant.chat.title} group "
                )

        if not all_complete:
            self.bot.reply_to(message, "Not all participants filled in "
                                       "the data ")
            return

        random.shuffle(participants)

        for i in range(len(participants)):
            receiving: Participation = participants[i]
            giving: Participation = participants[(i + 1) % len(participants)]

            self.bot.send_message(
                giving.user.telegram_id,
                f"User: @{receiving.user.username}\n"
                f"My hobby is: {receiving.text_1}\n"
                f"I want to get: {receiving.text_2}\n"
                f"I don't want to get: {receiving.text_3}\n"
            )

        ChatManager(self.db).set_status(chat, ChatStatus.RECORDS_SENT)
