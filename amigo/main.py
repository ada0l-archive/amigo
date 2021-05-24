import sys

import amigo.env
from amigo.core import Bot
from amigo.database import DataBase


def show_help():
    print("commands:\n"
          "\tcreate_all     - define tables\n"
          "\tdrop_all       - drop tables\n"
          "\trun            - run bot"
          "\tcreate_and_run - define tables and run")


def create_all():
    db = DataBase(amigo.env.DATABASE_URL, echo=False)
    db.create_all()


def drop_all():
    db = DataBase(amigo.env.DATABASE_URL, echo=False)
    db.drop_all()


def run():
    db = DataBase(amigo.env.DATABASE_URL, echo=False)
    bot = Bot(env=amigo.env, db=db, log=True)
    bot.run()


def cannot_recognize():
    print("I can't recognize what you want")
    show_help()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        cannot_recognize()
        exit(1)
    first_param = sys.argv[1]
    if first_param == "create_all":
        create_all()
    elif first_param == "drop_all":
        drop_all()
    elif first_param == "run":
        run()
    elif first_param == "create_and_run":
        create_all()
        run()
    elif first_param == "help":
        show_help()
    else:
        cannot_recognize()
        exit(1)
