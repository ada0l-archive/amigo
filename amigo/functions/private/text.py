from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager, CurrentUserChatManager, \
    ParticipationManager
from amigo.models import User, Participation, ParticipationStatus


class PrivateText(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"func": cls.is_private}

    def main(self, message):
        user = ModelManager(self.db, User).get_object(
            telegram_id=message.chat.id
        )
        current_user_chat = CurrentUserChatManager(self.db).get_object(
            user=user
        )
        if not current_user_chat or not current_user_chat.chat:
            self.bot.reply_to(message, "I dont understand what you want")
            return

        participation = ModelManager(self.db, Participation).get_object(
            user=user,
            chat=current_user_chat.chat
        )

        if participation.status is ParticipationStatus.TEXT_1:
            ParticipationManager(self.db).set_text_1(
                participation=participation,
                text=message.text
            )
            self.bot.reply_to(message, "OK, what do you want to get?")
        elif participation.status is ParticipationStatus.TEXT_2:
            ParticipationManager(self.db).set_text_2(
                participation=participation,
                text=message.text
            )
            self.bot.reply_to(message, "OK, what don't you want to get?")
        elif participation.status is ParticipationStatus.TEXT_3:
            ParticipationManager(self.db).set_text_3(
                participation=participation,
                text=message.text
            )
            self.bot.reply_to(message, "OK, complete")
