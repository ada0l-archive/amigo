from amigo.database import DataBase
from amigo.managers.model_manager import ModelManager
from amigo.models import CurrentUserChat


class CurrentUserChatManager(ModelManager):

    def __init__(self, db: DataBase):
        super().__init__(db, CurrentUserChat)

    def set_chat(self, new_chat, user):
        instance, _ = self.create(
            allow_duplication=False,
            user=user
        )
        instance.chat = new_chat
        self.db.session.commit()
        return instance
