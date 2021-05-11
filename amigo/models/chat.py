import enum

from sqlalchemy import Column, Integer, Text, Enum

from amigo.models.base import BaseModel


class ChatStatus(enum.Enum):
    STARTED = 0
    RECORDS_SENT = 1
    SENDERS_COMPROMISED = 2


class Chat(BaseModel):
    __tablename__ = 'chat'
    telegram_id = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    status = Column(Enum(ChatStatus), nullable=False,
                    default=ChatStatus.STARTED)

    def __init__(self, telegram_id, title):
        self.telegram_id = telegram_id
        self.title = title

    def __str__(self):
        return f'<Chat({self.title})>'
