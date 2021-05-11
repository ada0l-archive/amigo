from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager, CurrentUserChatManager, \
    ParticipationManager
from amigo.models import User, Participation


class PrivateEdit(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["edit", ], "func": cls.is_private}

    def main(self, message):
        user = ModelManager(self.db, User).get_object(
            telegram_id=message.chat.id
        )
        current_user_chat = CurrentUserChatManager(self.db).get_object(
            user=user
        )
        if not current_user_chat:
            self.bot.reply_to(message, "You dont choose some chat")
            return
        participation = ModelManager(self.db, Participation).get_object(
            user=user,
            chat=current_user_chat.chat
        )
        ParticipationManager(self.db).drop_status(participation=participation)
        self.bot.reply_to(message, "What are your hobbies?")
