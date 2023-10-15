#!/usr/bin/python3

""" BaseModel Class"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for instances objects for the HBnBConsole
    Attribute:
        id:(str) - use uuid.uuid4() to create a unique id of instance
        created_at:  datetime when an instance is created
        updated_at: current datetime of an instance creation and update
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise creation of new instance of the BaseModel class

        Args:
            *args: variable length argument list
            **kwargs: Keyword argument for __init__ attributes
                -created_at(str): ISO format: creation time
                -updated_at(str): ISO format: update time
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            """
            when kwarg is empty
                -generates a unique id using uuid.uuid4()
                -sets created_at and updated_at
            """
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        """
        returns string representation of instance created
        str: A formatted string containing class
        [<class name>] (<self.id>) <self.__dict__>
        format: name, id, and attribute dictionary.
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at: current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        converts instance to a dictionary representation (object_dict)

        returns:
            -dictionary containing all keys/values of __dict__ of the instance
            -class name __class__.__name__
            -created_at(str): isoformat
            -updated_at(str): isoformat
        """

        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
