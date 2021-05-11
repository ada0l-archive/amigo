from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager, CurrentUserChatManager
from amigo.models import User, Chat


class PrivateSetCurrentUserChat(BaseFunction):

    @classmethod
    def info(cls):
        return "callback_query", {"func": lambda call: True}

    def main(self, call):
        user = ModelManager(self.db, User).get_object(
            telegram_id=call.message.chat.id
        )
        chat = ModelManager(self.db, Chat).get_object(
            id=call.data
        )
        CurrentUserChatManager(self.db).set_chat(
            new_chat=chat,
            user=user
        )
        self.bot.send_message(call.message.chat.id, f"Chosen {chat.title}")
