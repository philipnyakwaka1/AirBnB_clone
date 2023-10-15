#!/usr/bin/python3
"""This module defines the unittest for base_model.py module"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import os
import json


class TestBaseModel_initialization(unittest.TestCase):

    """This is a test class for the BaseModel"""

    def test_type_BaseModel(self):
        """test for type BaseModel"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_type_created_at_is_datetime(self):
        """tests if attribute created_at is datetime object"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_str(self):
        """This module tests for correct output of the __str__ method"""
        dt = datetime.today()
        d = dt.isoformat()
        user = BaseModel("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertIn("[BaseModel] (1)", user.__str__())
        self.assertIn("'created_at': " + repr(dt),  user.__str__())
        self.assertIn("'updated_at': " + repr(dt),  user.__str__())

    def test_type_updated_at_is_datetime(self):
        """tests if attribute updated_at is datetime object"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_if_id_is_string(self):
        """This method tests if an instance is of type BaseModel"""
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_ids(self):
        """This method tests for the uniqueness of user id"""

        id_list = []
        for i in range(200):
            user = BaseModel()
            id_list.append(user.id)
        self.assertEqual(len(id_list), len(set(id_list)))

    def test_different_created_at(self):
        """unittest for differnt created_at attributes"""

        user1 = BaseModel()
        sleep(0.05)
        user2 = BaseModel()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """unittest for differnt updated_at attributes"""

        user1 = BaseModel()
        sleep(0.05)
        user2 = BaseModel()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_save_method(self):
        """unittest for the save method"""
        user = BaseModel()
        update0 = user.updated_at
        user.save()
        update1 = user.updated_at
        self.assertNotEqual(update0, update1)

    def test_kwargs_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = BaseModel(id="1", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "1")
        self.assertEqual(user.created_at.isoformat(), dt_iso)
        self.assertEqual(user.updated_at.isoformat(), dt_iso)

    def test_kwargs_and_args_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        d = dt.isoformat()
        d_value = dt.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        user = BaseModel("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertEqual(user.id, "1")
        self.assertEqual(user.created_at, d_value)
        self.assertEqual(user.updated_at, d_value)
        self.assertEqual(user.created_at, d_value)
        self.assertEqual(user.updated_at, d_value)


class TestBaseModel_to_dict(unittest.TestCase):
    """This is a test class for the to_dict"""

    def test_type_of_to_dict(self):
        """test is to_dict is type dict"""

        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_correct_attributes(self):
        """tests if the dict has correct attributes"""

        self.assertIn("id", BaseModel().to_dict())
        self.assertIn("created_at", BaseModel().to_dict())
        self.assertIn("updated_at", BaseModel().to_dict())
        self.assertIn("__class__", BaseModel().to_dict())

    def test_added_attributes(self):
        """tests for existence of added attributes"""

        user = BaseModel()
        user.name = "Philip"
        user.age = 24
        self.assertIn("name", user.to_dict())
        self.assertIn("age", user.to_dict())

    def test_key_value_pair(self):
        """tests for correct key, value pairs"""

        dt = datetime.today()
        d = dt.isoformat()
        user = BaseModel("23", d, d, id="1", created_at=d, updated_at=d)
        user.name = "Philip"
        user.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'BaseModel',
            'name': 'Philip',
            'age': 24
        }
        self.assertDictEqual(user.to_dict(), my_dict)

    def test_dict_value_types(self):
        """test the type of dict values"""

        self.assertEqual(type(BaseModel().to_dict()['id']), str)
        self.assertEqual(type(BaseModel().to_dict()['created_at']), str)
        self.assertEqual(type(BaseModel().to_dict()['updated_at']), str)
        self.assertEqual(type(BaseModel().to_dict()['__class__']), str)

    def compare_to_dict_and__dict__(self):
        """compares to_dict() with __dict__"""

        self.assertNotEqual(BaseModel().to_dict(), BaseModel().__dict__())


class TestBaseModel_save(unittest.TestCase):
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

        user = BaseModel()
        update0 = user.updated_at
        user.save()
        update1 = user.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        user = BaseModel(id="1", created_at=d, updated_at=d)
        user.name = "Philip"
        user.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'BaseModel',
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
