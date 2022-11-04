#!/usr/bin/python3
""" class base """


from datetime import datetime
import uuid
import models


class BaseModel():
    '''
    Class BaseModel that defines all
    common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        Class constructor
        '''

        if not kwargs == {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        ''' __str__ method that returns a class description '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Public instance methods that
        returns a dictionary containing all keys/values.
        """
        dictionary = {}
        dictionary['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
