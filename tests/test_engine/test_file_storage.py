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
        self.assertEqual(str, type(FileStorage._FileStorage.__file_path))

    def test_if_file_object_is_dict(self):
        """This method tests if an instance is of type FileStorage"""
        self.assertEqual(dict, type(FileStorage._FileStorage.__object))


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

if __name__ == "__main__":
    unittest.main()
    
