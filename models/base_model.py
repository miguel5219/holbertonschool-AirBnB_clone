#!/usr/bin/python3
""" class base """


import datetime
from uuid import uuid4
import models


class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "update_at"]:
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Public instance methods that
        returns a dictionary containing all keys/values.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
