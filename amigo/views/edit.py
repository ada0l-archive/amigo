import telebot

from amigo.models import User, Participation, ModelManager
from amigo.views.base import BaseView


class EditView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["edit", ]}

    def group(self, message):
        self.bot.reply_to(message, "This command works only in private")

    def private(self, message):
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        chats = ModelManager(self.db, Participation).get_objects(
            filter={
                "user": ModelManager(self.db, User).get_object(
                    filter={
                        "telegram_id": message.from_user.id
                    })
            })

        if not chats:
            self.bot.reply_to(message, "You dont participate in any group")
            return

        list_of_chats = []
        for item in chats:
            list_of_chats.append(
                telebot.types.InlineKeyboardButton(
                    self.bot.get_chat(chat_id=item.chat.telegram_id).title,
                    callback_data=item.chat.id
                )
            )
        markup.add(*list_of_chats)
        self.bot.reply_to(message, "Choose some chat:", reply_markup=markup)
