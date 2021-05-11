from amigo.managers.model_manager import ModelManager
from amigo.database import DataBase
from amigo.models import Chat


class ChatManager(ModelManager):

    def __init__(self, db: DataBase):
        super().__init__(db, Chat)

    def set_status(self, instance, status):
        instance.status = status
        self.db.session.commit()
