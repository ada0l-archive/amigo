import functools
from abc import ABC

import telebot
from telebot.types import CallbackQuery

from amigo.models import ModelManager, Chat


class BaseView(ABC):
    def __init__(self, env, bot, db):
        self.env = env
        self.bot = bot
        self.db = db

    @staticmethod
    def is_group(message):
        if isinstance(message, CallbackQuery):
            message = message.message
        return message and (message.chat.type == 'group' or
                            message.chat.type == 'supergroup')

    @staticmethod
    def is_private(message):
        if isinstance(message, CallbackQuery):
            message = message.message
        return message and message.chat.type == 'private'

    @staticmethod
    def info():
        """
        Return information about routing of this command
        :return: tuple, first element is handle type, second arguments to handle
        """
        return "message", {"commands": ["example", ]}

    @classmethod
    def init(cls, env, bot, db):
        """
        Returns the function to pass to the handle
        :param env, through this param you can access the environment variables
        :param bot is an istance of the Bot class
        :param db is an istance of the database's connection
        :return Returns an instance of a main function
        """
        instance = cls(env, bot, db)
        return instance.main

    def main(self, message):
        try:
            if self.is_private(message):
                self.private(message)
            if self.is_group(message):
                self.group(message)
        except Exception as e:
            print(e)
            self.bot.reply_to(message, "Something went wrong.")

    def group(self, message):
        pass

    def private(self, message):
        pass

    def next(self, message, func):
        func.init(self.env, self.bot, self.db)(message)

    def get_markup_with_link_to_me(self):
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            telebot.types.InlineKeyboardButton(
                "Send me message",
                url=f"https://t.me/{self.bot.get_me().username}"
            )
        )
        return markup
