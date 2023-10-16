#!/usr/bin/python3
"""Base Model Class"""

import uuid
from datetime import datetime


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
        Initialise a new instance of the BaseModel class
        Args:
            *args: variable length arg list
            **kwargs: Keyword argument for __init__ attributes
        """

        if not kwargs:
            import __init__
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            __init__.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        returns a string rep of insatnce created

        Returns:
        str: A formatted string containing class
        [<class name>]
        (<self.id>)
        <self.__dict__>
        name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute  with the current datetime
        """
        import __init__
        self.updated_at = datetime.now()
        __init__.storage.save()

    def to_dict(self):
        """
        converts instance to a dictionary rep (object_dic)

        returns
         a dictionary containing all keys/values of __dict__ of the instance
            -a key __class__ must be added to this dict with name
            -created_at and updated_at converted to string object in ISO format
            format: %Y-%m-%dT%H:%M:%S.%f isoformat()
        """
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
