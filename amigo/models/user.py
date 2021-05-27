from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from amigo.models.participation import Participation
from amigo.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    telegram_id = Column(Integer, nullable=False)
    username = Column(Text, nullable=True)
    participation = relationship(Participation, cascade="all,delete")

    def __init__(self, telegram_id, username):
        self.telegram_id = telegram_id
        self.username = username

    def __str__(self):
        return f'<User(@{self.username})>'
