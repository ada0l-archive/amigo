import re

from amigo.models import User, Participation, ModelManager, \
    Chat
from amigo.views.base import BaseView


class TextView(BaseView):

    @classmethod
    def info(cls):
        return "callback_query", {"func": lambda call: True}

    def group(self, message):
        pass

    def _modify_commands(func):
        def wrapper(self, message, *args, **kwargs):
            skip = False
            if re.match('^/cancel', message.text) is not None:
                self.bot.reply_to(message, "Canceled")
                return
            if re.match('^/skip', message.text) is not None:
                skip = True
            value = func(self, message=message, skip=skip, *args, **kwargs)
            return value

        return wrapper

    @staticmethod
    def get_old_data(text):
        if text != "":
            return f"\n{text}\nWrite /skip to skip this field."
        return ""

    def private(self, call):
        user = ModelManager(self.db, User).get_object(
            filter={
                "telegram_id": call.message.chat.id
            })
        chat = ModelManager(self.db, Chat).get_object(
            filter={
                "id": call.data
            })

        participation = ModelManager(self.db, Participation).get_object(
            filter={
                "user": user,
                "chat": chat
            }
        )

        self.bot.register_next_step_handler(
            self.bot.send_message(
                call.message.chat.id,
                f"Hello, What are you hobbies? {self.get_old_data(participation.hobby)}"
            ),
            self.set_hobby,
            participation=participation
        )

    @_modify_commands
    def set_hobby(self, message, participation, skip=False):
        if skip is False:
            ModelManager(self.db, Participation).update_obj(
                obj=participation,
                values={
                    "hobby": message.text
                })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                f"OK, what do you want to get? {self.get_old_data(participation.wishes)}"
            ),
            self.set_wishes,
            participation=participation
        )

    @_modify_commands
    def set_wishes(self, message, participation, skip=False):
        if skip is False:
            ModelManager(self.db, Participation).update_obj(
                obj=participation,
                values={
                    "wishes": message.text
                })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                f"OK, what don't you want to get? {self.get_old_data(participation.not_wishes)}"
            ),
            self.set_not_wishes,
            participation=participation
        )

    @_modify_commands
    def set_not_wishes(self, message, participation, skip=False):
        if skip is False:
            ModelManager(self.db, Participation).update_obj(
                obj=participation,
                values={
                    "not_wishes": message.text
                })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                f"OK, What is your address? {self.get_old_data(participation.address)}"
            ),
            self.set_address,
            participation=participation
        )

    @_modify_commands
    def set_address(self, message, participation, skip=False):
        if skip is False:
            ModelManager(self.db, Participation).update_obj(
                obj=participation,
                values={
                    "address": message.text
                })

        self.bot.send_message(
            message.chat.id,
            "OK, I filled in all the data."
        )