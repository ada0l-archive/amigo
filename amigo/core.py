"""Bot class module"""

import logging

import telebot

import amigo.functions


class Bot:
    """Bot class"""
    def __init__(self, env, db, log=False):
        token = env.TELEGRAM_BOT_TOKEN

        self.env = env
        self.bot = telebot.TeleBot(token)
        self.db = db

        if log:
            telebot.logger.setLevel(logging.DEBUG)

        self.functions = []

    def run(self):
        """run the bot"""
        self._register_actions()
        self.bot.polling()

    def _discover_functions(self):
        for func in dir(amigo.functions):
            if str(func).startswith('_'):
                break
            obj = getattr(amigo.functions, func)
            self.functions.append(obj)

    def _register_actions(self):
        self._discover_functions()

        for klass in self.functions:
            routing_info = klass.info()

            trigger_info = routing_info[0]
            handler_info = routing_info[1]

            m_handler = None
            if trigger_info == "message":
                m_handler = self.bot.message_handler(**handler_info)
            elif trigger_info == "callback_query":
                m_handler = self.bot.callback_query_handler(**handler_info)
            elif trigger_info == "inline_query":
                m_handler = self.bot.inline_handler(**handler_info)
            m_handler(klass.init(env=self.env, bot=self.bot, db=self.db))
