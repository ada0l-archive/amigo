import enum

from sqlalchemy import Column, Integer, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from amigo.models.participation import Participation
from amigo.models.base import BaseModel
from amigo.models.user import User


class ChatStatus(enum.Enum):
    STARTED = 0
    RECORDS_SENT = 1
    SENDERS_COMPROMISED = 2


class Chat(BaseModel):
    __tablename__ = 'chat'
    telegram_id = Column(Integer, nullable=False)
    status = Column(Enum(ChatStatus), nullable=False,
                    default=ChatStatus.STARTED)

    organizer_id = Column(Integer, ForeignKey(User.id), nullable=True)
    organizer = relationship('User', foreign_keys='Chat.organizer_id')
    participation = relationship(Participation, cascade="all,delete")

    is_offline_event = Column(Boolean, default=False, nullable=True)

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id

    def __str__(self):
        return f'<Chat({self.telegram_id})>'
