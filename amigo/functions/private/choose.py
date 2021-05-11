import telebot

from amigo.functions.base_functions import BaseFunction
from amigo.managers import ModelManager
from amigo.models import Participation, User


class PrivateChoose(BaseFunction):

    @classmethod
    def info(cls):
        return "message", {"commands": ["choose", ], "func": cls.is_private}

    def main(self, message):
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        chats = ModelManager(self.db, Participation).get_objects(
            user=ModelManager(self.db, User).get_object(
                telegram_id=message.from_user.id
            )
        )

        if not chats:
            self.bot.reply_to(message, "You dont participate in any group")
            return

        list_of_chats = []
        for item in chats:
            list_of_chats.append(
                telebot.types.InlineKeyboardButton(
                    item.chat.title, callback_data=item.chat.id)
            )
        markup.add(*list_of_chats)
        self.bot.reply_to(message, "Choose some chat:", reply_markup=markup)
