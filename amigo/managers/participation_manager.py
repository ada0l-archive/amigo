from amigo.database import DataBase
from amigo.managers.model_manager import ModelManager
from amigo.models import CurrentUserChat, ParticipationStatus


class ParticipationManager(ModelManager):

    def __init__(self, db: DataBase):
        super().__init__(db, CurrentUserChat)

    def drop_status(self, participation):
        participation.status = ParticipationStatus.TEXT_1
        self.db.session.commit()

    def set_text_1(self, participation, text):
        participation.text_1 = text
        participation.status = ParticipationStatus.TEXT_2
        self.db.session.commit()

    def set_text_2(self, participation, text):
        participation.text_2 = text
        participation.status = ParticipationStatus.TEXT_3
        self.db.session.commit()

    def set_text_3(self, participation, text):
        participation.text_3 = text
        participation.status = ParticipationStatus.COMPLETE
        self.db.session.commit()