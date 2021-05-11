import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

from amigo.models.base import BaseModel
from amigo.models.chat import Chat
from amigo.models.user import User


class ParticipationStatus(enum.Enum):
    TEXT_1 = 0
    TEXT_2 = 1
    TEXT_3 = 2
    COMPLETE = 3


class Participation(BaseModel):
    __tablename__ = 'participation'
    user_id = Column(Integer, ForeignKey(User.id))
    chat_id = Column(Integer, ForeignKey(Chat.id))
    user = relationship('User', foreign_keys='Participation.user_id')
    chat = relationship('Chat', foreign_keys='Participation.chat_id')
    status = Column(Enum(ParticipationStatus), nullable=True,
                    default=None)
    text_1 = Column(Text, nullable=False, default="")
    text_2 = Column(Text, nullable=False, default="")
    text_3 = Column(Text, nullable=False, default="")

    def __str__(self):
        return f'<Participation(@{self.user.username}, {self.chat.title})>'
