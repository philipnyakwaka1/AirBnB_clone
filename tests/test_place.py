#!/usr/bin/python3
"""This module defines the unittest for place.py module"""
import unittest
from datetime import datetime
from models.place import Place
from time import sleep
import os
import json


class TestPlace_initialization(unittest.TestCase):
    """This is a test class for the Place"""

    def test_type_Place(self):
        """test for type Place"""
        self.assertEqual(Place, type(Place()))

    def test_type_created_at_is_datetime(self):
        """tests if attribute created_at is datetime object"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_public_class_attributes(self):
        """tests for presence of public class attributes"""

        self.assertIn("city_id", dir(Place()))
        self.assertIn("user_id", dir(Place()))
        self.assertIn("name", dir(Place()))
        self.assertIn("description", dir(Place()))
        self.assertIn("number_rooms", dir(Place()))
        self.assertIn("number_bathrooms", dir(Place()))
        self.assertIn("max_guest", dir(Place()))
        self.assertIn("price_by_night", dir(Place()))
        self.assertIn("latitude", dir(Place()))
        self.assertIn("longitude", dir(Place()))
        self.assertIn("amenity_ids", dir(Place()))
        self.assertNotIn("city_id", Place().__dict__)
        self.assertNotIn("user_id", Place().__dict__)
        self.assertNotIn("name", Place().__dict__)
        self.assertNotIn("description", Place().__dict__)
        self.assertNotIn("number_rooms", Place().__dict__)
        self.assertNotIn("number_bathrooms", Place().__dict__)
        self.assertNotIn("max_guest", Place().__dict__)
        self.assertNotIn("price_by_night", Place().__dict__)
        self.assertNotIn("latitude", Place().__dict__)
        self.assertNotIn("longitude", Place().__dict__)
        self.assertNotIn("amenity_ids", Place().__dict__)
        self.assertEqual(str, type(Place().city_id))
        self.assertEqual(str, type(Place().user_id))
        self.assertEqual(str, type(Place().name))
        self.assertEqual(str, type(Place().description))
        self.assertEqual(int, type(Place().number_rooms))
        self.assertEqual(int, type(Place().number_bathrooms))
        self.assertEqual(int, type(Place().max_guest))
        self.assertEqual(int, type(Place().price_by_night))
        self.assertEqual(float, type(Place().latitude))
        self.assertEqual(float, type(Place().longitude))
        self.assertEqual(list, type(Place().amenity_ids))
        for i in Place().amenity_ids:
            self.assertEqual(str, type(Place().amenity_ids[i]))

    def test_str(self):
        """This module tests for correct output of the __str__ method"""
        dt = datetime.today()
        d = dt.isoformat()
        ct = Place("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertIn("[Place] (1)", ct.__str__())
        self.assertIn("'created_at': " + repr(dt),  ct.__str__())
        self.assertIn("'updated_at': " + repr(dt),  ct.__str__())

    def test_type_updated_at_is_datetime(self):
        """tests if attribute updated_at is datetime object"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_if_id_is_string(self):
        """This method tests if an instance is of type Place"""
        self.assertEqual(str, type(Place().id))

    def test_unique_ids(self):
        """This method tests for the uniqueness of ct id"""

        id_list = []
        for i in range(200):
            ct = Place()
            id_list.append(ct.id)
        self.assertEqual(len(id_list), len(set(id_list)))

    def test_different_created_at(self):
        """unittest for differnt created_at attributes"""

        ct1 = Place()
        sleep(0.05)
        ct2 = Place()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_different_updated_at(self):
        """unittest for differnt updated_at attributes"""

        ct1 = Place()
        sleep(0.05)
        ct2 = Place()
        self.assertLess(ct1.updated_at, ct2.updated_at)

    def test_kwargs_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        ct = Place(id="1", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ct.id, "1")
        self.assertEqual(ct.created_at.isoformat(), dt_iso)
        self.assertEqual(ct.updated_at.isoformat(), dt_iso)

    def test_kwargs_and_args_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        d = dt.isoformat()
        d_value = dt.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        ct = Place("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertEqual(ct.id, "1")
        self.assertEqual(ct.created_at, d_value)
        self.assertEqual(ct.updated_at, d_value)


class TestPlace_to_dict(unittest.TestCase):
    """This is a test class for the to_dict"""

    def test_type_of_to_dict(self):
        """test is to_dict is type dict"""

        self.assertEqual(dict, type(Place().to_dict()))

    def test_correct_attributes(self):
        """tests if the dict has correct attributes"""

        self.assertIn("id", Place().to_dict())
        self.assertIn("created_at", Place().to_dict())
        self.assertIn("updated_at", Place().to_dict())
        self.assertIn("__class__", Place().to_dict())

    def test_added_attributes(self):
        """tests for existence of added attributes"""

        ct = Place()
        ct.name = "Nairobi"
        ct.no = 24
        self.assertIn("name", ct.to_dict())
        self.assertIn("no", ct.to_dict())

    def test_key_value_pair(self):
        """tests for correct key, value pairs"""

        dt = datetime.today()
        d = dt.isoformat()
        ct = Place("23", d, d, id="1", created_at=d, updated_at=d)
        ct.name = "Nairobi"
        ct.no = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'Place',
            'name': 'Nairobi',
            'no': 24
        }
        self.assertDictEqual(ct.to_dict(), my_dict)

    def test_dict_value_types(self):
        """test the type of dict values"""

        self.assertEqual(type(Place().to_dict()['id']), str)
        self.assertEqual(type(Place().to_dict()['created_at']), str)
        self.assertEqual(type(Place().to_dict()['updated_at']), str)
        self.assertEqual(type(Place().to_dict()['__class__']), str)

    def compare_to_dict_and__dict__(self):
        """compares to_dict() with __dict__"""

        self.assertNotEqual(Place().to_dict(), Place().__dict__())


class TestPlace_save(unittest.TestCase):
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

        ct = Place()
        update0 = ct.updated_at
        ct.save()
        update1 = ct.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        ct = Place(id="1", created_at=d, updated_at=d)
        ct.name = "Nairobi"
        ct.no = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'Place',
            'name': 'Nairobi',
            'no': 24
        }
        ct.save()
        with open("file.json", "r") as f:
            self.assertIsInstance(json.load(f), dict)

        """
        ct.save()
        with open("file.json", "r") as f:
            key = f"{ct.__class__.__name__}.{ct.id}"
            self.assertDictEqual(json.load(f)[key], my_dict)
        """


if __name__ == "__main__":
    unittest.main()