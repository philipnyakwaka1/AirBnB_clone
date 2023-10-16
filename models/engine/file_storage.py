#!/usr/bin/env python

"""Module defines FileStorage class for hbnb clone storage management"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """stores data through serialization and deserialization in JSON
    Attributes:
    __file_path = "file.json"
    __objects = empty dictionary
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
         returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
         args : obj(BaseModel ) Object added
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
          serializes __objects to the JSON file (path: __file_path)
        """
        data = FileStorage.__objects
        objdict = {}

        for key, obj in data.items():
            objdict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """
          deserializes the JSON file to __objects,
          (only if the JSON file (__file_path) exists ; otherwise, do nothing.
          If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
