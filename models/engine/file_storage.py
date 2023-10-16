#!/usr/bin/env python

"""Module defines FileStorage class for hbnb clone storage management"""

import json
import os


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
        data = {}
        for key, obj in data.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

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
                    class_name, obj_id = key.split(".")
                    obj_class = globals()[class_name]
                    obj = obj_class(**value)
                    FileStorage.__objects[key] = new_obj

        except FileNotFoundError:
            pass
