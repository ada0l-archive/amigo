from amigo.database import DataBase


class ModelManager:

    def __init__(self, db: DataBase, obj):
        self.obj = obj
        self.db = db

    def get_objects(self, **kwargs):
        return self.db.session.query(self.obj).filter_by(
            **kwargs
        ).all()

    def get_object(self, **kwargs):
        return self.db.session.query(self.obj).filter_by(
            **kwargs
        ).first()

    def create(self, allow_duplication: bool = True,
               **kwargs) -> (object, bool):
        """
        returns the object itself and a boolean
        if the object already existed, then return false.
        if the object was created new, then return true.
        """
        instance = self.get_object(**kwargs)

        if not allow_duplication:
            if instance:
                return instance, False

        instance = self.obj(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance, True

    def delete(self, **kwargs) -> bool:
        """
        if the object was deleted, then return the truth,
        otherwise return false
        """
        instance = self.get_object(**kwargs)

        if instance:
            self.db.session.delete(instance)
            self.db.session.commit()
            return True

        return False
