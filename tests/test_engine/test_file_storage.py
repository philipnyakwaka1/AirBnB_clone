#!/usr/bin/python3
"""This module defines unit test for FileStorage Class"""

import os
import json
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.state import State
from models.user import User

class TestFileStorage_initialization(unittest.TestCase):

    """This is a test class for the FileStorage"""

    def test_type_FileStorage(self):
        """test for type FileStorage"""
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_if_file_path_is_string(self):
        """This method tests if an instance is of type FileStorage"""
        self.assertEqual(str, type(FileStorage().__file_path))

    def test_if_file_object_is_dict(self):
        """This method tests if an instance is of type FileStorage"""
        self.assertEqual(dict, type(FileStorage().__object))


class TestFileStorage_save(unittest.TestCase):
    """Test class for save method"""

    @classmethod
    def setUp(self):
        """renames the file.json file to avoid overwriting it"""
        try:
            os.rename("file.json", "tmp")
        except Exception as e:
            pass

    def tearDown(self):
        """renames tmp back to file.json to restore it"""

        try:
            os.remove("file.json")
            pass
        except Exception as e:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception as e:
            pass

    def test_updated_at(self):
        """unittest the save method for updated time"""

        user = FileStorage()
        update0 = user.updated_at
        user.save()
        update1 = user.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        user = FileStorage(id="1", created_at=d, updated_at=d)
        user.name = "Philip"
        user.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'FileStorage',
            'name': 'Philip',
            'age': 24
        }
        user.save()
        with open("file.json", "r") as f:
            self.assertIsInstance(json.load(f), dict)

        """
        user.save()
        with open("file.json", "r") as f:
            key = f"{user.__class__.__name__}.{user.id}"
            self.assertDictEqual(json.load(f)[key], my_dict)
        """


if __name__ == "__main__":
    unittest.main()
    
