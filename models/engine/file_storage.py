#!/usr/bin/python3
"""Module for FileStorage class"""

import json


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary object __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f, ensure_ascii=False)

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception as e:
            pass
