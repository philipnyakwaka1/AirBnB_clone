#!/usr/bin/python3
"""Base Model Class"""

import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    Base class for instances objects for the HBnB

    Attributes
        id: string - assign with an uuid when an instance is created uuid4()
        created_at: datetime - assign with the current datetime
        updated_at: datetime - assign with the updated datetime
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the Base class
        Arguments:
            kwargs: a dictionary representing the object
        """

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """returns string representation of instance created"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        my_dict['updated_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        return my_dict
