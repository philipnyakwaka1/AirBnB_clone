#!/usr/bin/python3
"""This module defines the unittest for user.py module"""
import unittest
from datetime import datetime
from models.user import User
from time import sleep
import os
import json


class TestUser_initialization(unittest.TestCase):
    """This is a test class for the User"""

    def test_type_User(self):
        """test for type User"""
        self.assertEqual(User, type(User()))

    def test_type_created_at_is_datetime(self):
        """tests if attribute created_at is datetime object"""
        self.assertEqual(datetime, type(User().created_at))

    def test_public_class_attributes(self):
        """tests for presence of public class attributes"""

        self.assertIn("email", dir(User()))
        self.assertIn("password", dir(User()))
        self.assertIn("first_name", dir(User()))
        self.assertIn("last_name", dir(User()))
        self.assertNotIn("email", User().__dict__)
        self.assertNotIn("password", User().__dict__)
        self.assertNotIn("first_name", User().__dict__)
        self.assertNotIn("last_name", User().__dict__)
        self.assertEqual(str, type(User().email))
        self.assertEqual(str, type(User().password))
        self.assertEqual(str, type(User().first_name))
        self.assertEqual(str, type(User().last_name))

    def test_str(self):
        """This module tests for correct output of the __str__ method"""
        dt = datetime.today()
        d = dt.isoformat()
        rv = User("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertIn("[User] (1)", rv.__str__())
        self.assertIn("'created_at': " + repr(dt),  rv.__str__())
        self.assertIn("'updated_at': " + repr(dt),  rv.__str__())

    def test_type_updated_at_is_datetime(self):
        """tests if attribute updated_at is datetime object"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_if_id_is_string(self):
        """This method tests if an instance is of type User"""
        self.assertEqual(str, type(User().id))

    def test_unique_ids(self):
        """This method tests for the uniqueness of rv id"""

        id_list = []
        for i in range(200):
            rv = User()
            id_list.append(rv.id)
        self.assertEqual(len(id_list), len(set(id_list)))

    def test_different_created_at(self):
        """unittest for differnt created_at attributes"""

        rv1 = User()
        sleep(0.05)
        rv2 = User()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_different_updated_at(self):
        """unittest for differnt updated_at attributes"""

        rv1 = User()
        sleep(0.05)
        rv2 = User()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_kwargs_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = User(id="1", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "1")
        self.assertEqual(rv.created_at.isoformat(), dt_iso)
        self.assertEqual(rv.updated_at.isoformat(), dt_iso)

    def test_kwargs_and_args_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        d = dt.isoformat()
        d_value = dt.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        rv = User("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertEqual(rv.id, "1")
        self.assertEqual(rv.created_at, d_value)
        self.assertEqual(rv.updated_at, d_value)


class TestUser_to_dict(unittest.TestCase):
    """This is a test class for the to_dict"""

    def test_type_of_to_dict(self):
        """test is to_dict is type dict"""

        self.assertEqual(dict, type(User().to_dict()))

    def test_correct_attributes(self):
        """tests if the dict has correct attributes"""

        self.assertIn("id", User().to_dict())
        self.assertIn("created_at", User().to_dict())
        self.assertIn("updated_at", User().to_dict())
        self.assertIn("__class__", User().to_dict())

    def test_added_attributes(self):
        """tests for existence of added attributes"""

        rv = User()
        rv.name = "Philip"
        rv.age = 24
        self.assertIn("name", rv.to_dict())
        self.assertIn("age", rv.to_dict())

    def test_key_value_pair(self):
        """tests for correct key, value pairs"""

        dt = datetime.today()
        d = dt.isoformat()
        rv = User("23", d, d, id="1", created_at=d, updated_at=d)
        rv.name = "Philip"
        rv.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'User',
            'name': 'Philip',
            'age': 24
        }
        self.assertDictEqual(rv.to_dict(), my_dict)

    def test_dict_value_types(self):
        """test the type of dict values"""

        self.assertEqual(type(User().to_dict()['id']), str)
        self.assertEqual(type(User().to_dict()['created_at']), str)
        self.assertEqual(type(User().to_dict()['updated_at']), str)
        self.assertEqual(type(User().to_dict()['__class__']), str)

    def compare_to_dict_and__dict__(self):
        """compares to_dict() with __dict__"""

        self.assertNotEqual(User().to_dict(), User().__dict__())


class TestUser_save(unittest.TestCase):
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

        rv = User()
        update0 = rv.updated_at
        rv.save()
        update1 = rv.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        rv = User(id="1", created_at=d, updated_at=d)
        rv.name = "Philip"
        rv.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'User',
            'name': 'Philip',
            'age': 24
        }
        rv.save()
        with open("file.json", "r") as f:
            self.assertIsInstance(json.load(f), dict)

        """
        rv.save()
        with open("file.json", "r") as f:
            key = f"{rv.__class__.__name__}.{rv.id}"
            self.assertDictEqual(json.load(f)[key], my_dict)
        """


if __name__ == "__main__":
    unittest.main()