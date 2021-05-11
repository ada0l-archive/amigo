from sqlalchemy import Column, Integer, Text

from amigo.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    telegram_id = Column(Integer, nullable=False)
    username = Column(Text, nullable=False)
    first_name = Column(Text, nullable=False)

    def __init__(self, telegram_id, username, first_name):
        self.telegram_id = telegram_id
        self.username = username
        self.first_name = first_name

    def __str__(self):
        return f'<User(@{self.username})>'
