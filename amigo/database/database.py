from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from amigo.database.base import Base


class DataBase:

    def __init__(self, url: str, echo=True):
        self.engine = create_engine(url, echo=echo)
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)
