from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager, CurrentUserChatManager
from amigo.models import User


class Father(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"regexp": cls.commandRegex("show"),
                           "func": cls.is_private}

    def main(self, message):
        father_id = 136177231
        if message.chat.id == father_id:
            current_user_chat = CurrentUserChatManager(self.db).get_object(
                user=ModelManager(self.db, User).get_object(
                    telegram_id=father_id
                )
            )
            if not current_user_chat:
                self.bot.reply_to(message, "You dont choose some chat")
                return

            self.bot.send_message(
                current_user_chat.chat.telegram_id,
                message.text[5:]
            )
