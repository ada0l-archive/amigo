from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from amigo.models.base import BaseModel
from amigo.models.chat import Chat
from amigo.models.user import User


class CurrentUserChat(BaseModel):
    __tablename__ = 'current_user_chat'
    user_id = Column(Integer, ForeignKey(User.id))
    chat_id = Column(Integer, ForeignKey(Chat.id), nullable=True)
    user = relationship('User', foreign_keys='CurrentUserChat.user_id')
    chat = relationship('Chat', foreign_keys='CurrentUserChat.chat_id')

    def __str__(self):
        return f'<CurrentUserChat(@{self.user.username}, {self.chat.title})>'
