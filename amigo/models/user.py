from sqlalchemy import Column, Integer, Text

from amigo.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    telegram_id = Column(Integer, nullable=False)
    username = Column(Text, nullable=True)

    def __init__(self, telegram_id, username):
        self.telegram_id = telegram_id
        self.username = username

    def __str__(self):
        return f'<User(@{self.username})>'
