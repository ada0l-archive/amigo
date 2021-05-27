import random

from amigo.models import Chat, Participation, ParticipationStatus, ChatStatus, \
    ModelManager
from amigo.views.base import BaseView


class SendView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["send", ]}

    def group(self, message):
        chat = ModelManager(self.db, Chat).get_object(
            filter={
                "telegram_id": message.chat.id
            })
        if not chat:
            self.bot.reply_to(message, "You dont started bot")
            return

        if chat.status != ChatStatus.STARTED:
            self.bot.reply_to(message, "Forms have already been sent ")
            return

        participants = ModelManager(self.db, Participation).get_objects(
            filter={
                "chat": chat
            })

        if len(participants) < 2:
            self.bot.reply_to(message, "There aren't enough participants")
            return

        chat_title = self.bot.get_chat(chat_id=chat.telegram_id).title

        all_complete = True

        not_filled_users = ""
        for participant in participants:
            if participant.hobby == "" or \
                    participant.wishes == "" or \
                    participant.not_wishes == "" or \
                    participant.address == "":
                all_complete = False
                not_filled_users += f"@{participant.user.username} "
                try:
                    self.bot.send_message(
                        participant.user.telegram_id,
                        "you didn't fill in the fields for the "
                        f"{chat_title} group "
                    )
                except Exception as _:
                    pass

        if not all_complete:
            self.bot.reply_to(
                message,
                "Not all participants filled in "
                f"the data. {not_filled_users}.",
                reply_markup=self.get_markup_with_link_to_me()
            )
            return

        random.shuffle(participants)

        all_info = ""
        for i in range(len(participants)):
            receiving: Participation = participants[i]
            giving: Participation = participants[(i + 1) % len(participants)]
            all_info += f"@{receiving.user.username} -> @{giving.user.username}\n"
            self.bot.send_message(
                giving.user.telegram_id,
                f"User: @{receiving.user.username}\n"
                f"My hobby is: {receiving.hobby}\n"
                f"I want to get: {receiving.wishes}\n"
                f"I don't want to get: {receiving.not_wishes}\n"
                f"My address: {receiving.address}\n"
            )

        if chat.organizer is not None:
            self.bot.send_message(
                chat.organizer.telegram_id,
                all_info
            )

        ModelManager(self.db, Chat).update(
            filter={
                "telegram_id": chat.telegram_id
            },
            values={
                "status": ChatStatus.RECORDS_SENT
            }
        )

    def private(self, message):
        self.bot.reply_to(message, "This command works only in groups")
