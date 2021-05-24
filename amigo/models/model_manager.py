from datetime import datetime, timezone

from amigo.database import DataBase
from amigo.models.base import BaseModel


class ModelManager:

    def __init__(self, db: DataBase, obj):
        self.obj = obj
        self.db = db

    def get_objects(self, filter: dict):
        return self.db.session.query(self.obj).filter_by(
            **filter
        ).all()

    def get_object(self, filter):
        return self.db.session.query(self.obj).filter_by(
            **filter
        ).first()

    def create(self, allow_duplication: bool = True,
               args: dict = None) -> (object, bool):
        """
        returns the object itself and a boolean
        if the object already existed, then return false.
        if the object was created new, then return true.
        """
        instance = self.get_object(args)

        if not allow_duplication:
            if instance:
                return instance, False

        instance = self.obj(**args)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance, True

    def update(self, filter: dict, values: dict) -> None:
        #values["updated_at"] = datetime.now(timezone.utc)
        self.db.session.query(self.obj).\
            filter_by(**filter).\
            update(values)
        self.db.session.commit()

    def update_obj(self, obj: BaseModel, values: dict) -> None:
        values["updated_at"] = datetime.now(timezone.utc)
        for key, value in values.items():
            setattr(obj, key, value)
        self.db.session.commit()

    def delete(self, filter) -> bool:
        """
        if the object was deleted, then return the truth,
        otherwise return false
        """
        instance = self.get_object(filter)

        if instance:
            self.db.session.delete(instance)
            self.db.session.commit()
            return True

        return False
