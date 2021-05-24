import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

from amigo.models.base import BaseModel
from amigo.models.chat import Chat
from amigo.models.user import User


class ParticipationStatus(enum.Enum):
    HOBBY = 0
    WISHES = 1
    NOT_WISHES = 2
    ADDRESS = 3
    COMPLETE = 4


class Participation(BaseModel):
    __tablename__ = 'participation'
    user_id = Column(Integer, ForeignKey(User.id))
    chat_id = Column(Integer, ForeignKey(Chat.id))
    user = relationship('User', foreign_keys='Participation.user_id')
    chat = relationship('Chat', foreign_keys='Participation.chat_id')
    status = Column(Enum(ParticipationStatus), nullable=True,
                    default=None)
    hobby = Column(Text, nullable=False, default="")
    wishes = Column(Text, nullable=False, default="")
    not_wishes = Column(Text, nullable=False, default="")
    address = Column(Text, nullable=False, default="")

    def __str__(self):
        return f'<Participation(@{self.user.username}, {self.chat.telegram_id})>'
