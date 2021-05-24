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

    def _cancel_decorator(  func):
        def wrapper(self, message, *args, **kwargs):
            if re.match('^/cancel', message.text) is not None:
                return
            value = func(self, message, *args, **kwargs)
            return value

        return wrapper

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
                "Hello, What are you hobbies?"
            ),
            self.set_hobby,
            participation=participation
        )

    @_cancel_decorator
    def set_hobby(self, message, participation):
        ModelManager(self.db, Participation).update_obj(
            obj=participation,
            values={
                "hobby": message.text
            })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                "OK, what do you want to get?"
            ),
            self.set_wishes,
            participation=participation
        )

    @_cancel_decorator
    def set_wishes(self, message, participation):
        ModelManager(self.db, Participation).update_obj(
            obj=participation,
            values={
                "wishes": message.text
            })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                "OK, what don't you want to get?"
            ),
            self.set_not_wishes,
            participation=participation
        )

    @_cancel_decorator
    def set_not_wishes(self, message, participation):
        ModelManager(self.db, Participation).update_obj(
            obj=participation,
            values={
                "not_wishes": message.text
            })

        self.bot.register_next_step_handler(
            self.bot.send_message(
                message.chat.id,
                "OK, What is your address?"
            ),
            self.set_address,
            participation=participation
        )

    @_cancel_decorator
    def set_address(self, message, participation):
        ModelManager(self.db, Participation).update_obj(
            obj=participation,
            values={
                "address": message.text
            })

        self.bot.send_message(
            message.chat.id,
            "OK, I filled in all the data."
        )