#!/usr/bin/python3
"""This module defines the unittest for amenity.py module"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from time import sleep
import os
import json


class TestAmenity_initialization(unittest.TestCase):
    """This is a test class for the Amenity"""

    def test_type_Amenity(self):
        """test for type Amenity"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_type_created_at_is_datetime(self):
        """tests if attribute created_at is datetime object"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_public_class_attributes(self):
        """tests for presence of public class attributes"""

        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", Amenity().__dict__)
        self.assertEqual(str, type(Amenity().name))

    def test_str(self):
        """This module tests for correct output of the __str__ method"""
        dt = datetime.today()
        d = dt.isoformat()
        amenity = Amenity("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertIn("[Amenity] (1)", amenity.__str__())
        self.assertIn("'created_at': " + repr(dt),  amenity.__str__())
        self.assertIn("'updated_at': " + repr(dt),  amenity.__str__())

    def test_type_updated_at_is_datetime(self):
        """tests if attribute updated_at is datetime object"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_if_id_is_string(self):
        """This method tests if an instance is of type Amenity"""
        self.assertEqual(str, type(Amenity().id))

    def test_unique_ids(self):
        """This method tests for the uniqueness of amenity id"""

        id_list = []
        for i in range(200):
            amenity = Amenity()
            id_list.append(amenity.id)
        self.assertEqual(len(id_list), len(set(id_list)))

    def test_different_created_at(self):
        """unittest for differnt created_at attributes"""

        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_different_updated_at(self):
        """unittest for differnt updated_at attributes"""

        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_kwargs_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="1", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "1")
        self.assertEqual(amenity.created_at.isoformat(), dt_iso)
        self.assertEqual(amenity.updated_at.isoformat(), dt_iso)

    def test_kwargs_and_args_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        d = dt.isoformat()
        d_value = dt.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        amenity = Amenity("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertEqual(amenity.id, "1")
        self.assertEqual(amenity.created_at, d_value)
        self.assertEqual(amenity.updated_at, d_value)


class TestAmenity_to_dict(unittest.TestCase):
    """This is a test class for the to_dict"""

    def test_type_of_to_dict(self):
        """test is to_dict is type dict"""

        self.assertEqual(dict, type(Amenity().to_dict()))

    def test_correct_attributes(self):
        """tests if the dict has correct attributes"""

        self.assertIn("id", Amenity().to_dict())
        self.assertIn("created_at", Amenity().to_dict())
        self.assertIn("updated_at", Amenity().to_dict())
        self.assertIn("__class__", Amenity().to_dict())

    def test_added_attributes(self):
        """tests for existence of added attributes"""

        amenity = Amenity()
        amenity.name = "Philip"
        amenity.age = 24
        self.assertIn("name", amenity.to_dict())
        self.assertIn("age", amenity.to_dict())

    def test_key_value_pair(self):
        """tests for correct key, value pairs"""

        dt = datetime.today()
        d = dt.isoformat()
        amenity = Amenity("23", d, d, id="1", created_at=d, updated_at=d)
        amenity.name = "Philip"
        amenity.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'Amenity',
            'name': 'Philip',
            'age': 24
        }
        self.assertDictEqual(amenity.to_dict(), my_dict)

    def test_dict_value_types(self):
        """test the type of dict values"""

        self.assertEqual(type(Amenity().to_dict()['id']), str)
        self.assertEqual(type(Amenity().to_dict()['created_at']), str)
        self.assertEqual(type(Amenity().to_dict()['updated_at']), str)
        self.assertEqual(type(Amenity().to_dict()['__class__']), str)

    def compare_to_dict_and__dict__(self):
        """compares to_dict() with __dict__"""

        self.assertNotEqual(Amenity().to_dict(), Amenity().__dict__())


class TestAmenity_save(unittest.TestCase):
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

        amenity = Amenity()
        update0 = amenity.updated_at
        amenity.save()
        update1 = amenity.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        amenity = Amenity(id="1", created_at=d, updated_at=d)
        amenity.name = "Philip"
        amenity.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'Amenity',
            'name': 'Philip',
            'age': 24
        }
        amenity.save()
        with open("file.json", "r") as f:
            self.assertIsInstance(json.load(f), dict)

        """"
        amenity.save()
        with open("file.json", "r") as f:
            key = f"{amenity.__class__.__name__}.{amenity.id}"
            self.assertDictEqual(json.load(f)[key], my_dict)
        """


if __name__ == "__main__":
    unittest.main()
