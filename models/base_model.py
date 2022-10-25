#!/usr/bin/python3
""" class base """


from datetime import datetime
import uuid


class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Public instance methods that
        returns a dictionary containing all keys/values.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["update_at"] = dic["updated_at"].isoformat()
        return dic
