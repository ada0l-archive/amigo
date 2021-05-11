from amigo.core import Bot
from amigo.database import DataBase
import amigo.env

if __name__ == "__main__":
    db = DataBase(amigo.env.DATABASE_URL, echo=False)
    db.create_all()
    bot = Bot(env=amigo.env, db=db)
    bot.run()
