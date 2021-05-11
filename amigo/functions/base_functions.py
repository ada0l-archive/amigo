from abc import ABC


class BaseFunction(ABC):
    def __init__(self, env, bot, db):
        self.env = env
        self.bot = bot
        self.db = db

    @staticmethod
    def is_group(message):
        return message and message.chat.type == 'group'

    @staticmethod
    def is_private(message):
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
        """
        Endpoint
        :param message
        """
        pass
