#!/usr/bin/python3
"""This module defines the unittest for state.py module"""
import unittest
from datetime import datetime
from models.state import State
from time import sleep
import os
import json


class TestState_initialization(unittest.TestCase):
    """This is a test class for the State"""

    def test_type_State(self):
        """test for type State"""
        self.assertEqual(State, type(State()))

    def test_type_created_at_is_datetime(self):
        """tests if attribute created_at is datetime object"""
        self.assertEqual(datetime, type(State().created_at))

    def test_public_class_attributes(self):
        """tests for presence of public class attributes"""

        self.assertIn("name", dir(State()))
        self.assertNotIn("name", State().__dict__)
        self.assertEqual(str, type(State().name))

    def test_str(self):
        """This module tests for correct output of the __str__ method"""
        dt = datetime.today()
        d = dt.isoformat()
        st = State("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertIn("[State] (1)", st.__str__())
        self.assertIn("'created_at': " + repr(dt),  st.__str__())
        self.assertIn("'updated_at': " + repr(dt),  st.__str__())

    def test_type_updated_at_is_datetime(self):
        """tests if attribute updated_at is datetime object"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_if_id_is_string(self):
        """This method tests if an instance is of type State"""
        self.assertEqual(str, type(State().id))

    def test_unique_ids(self):
        """This method tests for the uniqueness of st id"""

        id_list = []
        for i in range(200):
            st = State()
            id_list.append(st.id)
        self.assertEqual(len(id_list), len(set(id_list)))

    def test_different_created_at(self):
        """unittest for differnt created_at attributes"""

        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_different_updated_at(self):
        """unittest for differnt updated_at attributes"""

        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_kwargs_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="1", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "1")
        self.assertEqual(st.created_at.isoformat(), dt_iso)
        self.assertEqual(st.updated_at.isoformat(), dt_iso)

    def test_kwargs_and_args_initialization(self):
        """unittest for initialization using kwargs"""

        dt = datetime.today()
        d = dt.isoformat()
        d_value = dt.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        st = State("23", d, d, id="1", created_at=d, updated_at=d)
        self.assertEqual(st.id, "1")
        self.assertEqual(st.created_at, d_value)
        self.assertEqual(st.updated_at, d_value)


class TestState_to_dict(unittest.TestCase):
    """This is a test class for the to_dict"""

    def test_type_of_to_dict(self):
        """test is to_dict is type dict"""

        self.assertEqual(dict, type(State().to_dict()))

    def test_correct_attributes(self):
        """tests if the dict has correct attributes"""

        self.assertIn("id", State().to_dict())
        self.assertIn("created_at", State().to_dict())
        self.assertIn("updated_at", State().to_dict())
        self.assertIn("__class__", State().to_dict())

    def test_added_attributes(self):
        """tests for existence of added attributes"""

        st = State()
        st.name = "Philip"
        st.age = 24
        self.assertIn("name", st.to_dict())
        self.assertIn("age", st.to_dict())

    def test_key_value_pair(self):
        """tests for correct key, value pairs"""

        dt = datetime.today()
        d = dt.isoformat()
        st = State("23", d, d, id="1", created_at=d, updated_at=d)
        st.name = "Philip"
        st.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'State',
            'name': 'Philip',
            'age': 24
        }
        self.assertDictEqual(st.to_dict(), my_dict)

    def test_dict_value_types(self):
        """test the type of dict values"""

        self.assertEqual(type(State().to_dict()['id']), str)
        self.assertEqual(type(State().to_dict()['created_at']), str)
        self.assertEqual(type(State().to_dict()['updated_at']), str)
        self.assertEqual(type(State().to_dict()['__class__']), str)

    def compare_to_dict_and__dict__(self):
        """compares to_dict() with __dict__"""

        self.assertNotEqual(State().to_dict(), State().__dict__())


class TestState_save(unittest.TestCase):
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

        st = State()
        update0 = st.updated_at
        st.save()
        update1 = st.updated_at
        self.assertNotEqual(update0, update1)

    def test_contents_saved_file(self):
        """Test the contents of saved files"""
        dt = datetime.today()
        d = dt.isoformat()
        st = State(id="1", created_at=d, updated_at=d)
        st.name = "Philip"
        st.age = 24
        my_dict = {
            'id': '1',
            'created_at': d,
            'updated_at': d,
            '__class__': 'State',
            'name': 'Philip',
            'age': 24
        }
        st.save()
        with open("file.json", "r") as f:
            self.assertIsInstance(json.load(f), dict)

        """
        st.save()
        with open("file.json", "r") as f:
            key = f"{st.__class__.__name__}.{st.id}"
            self.assertDictEqual(json.load(f)[key], my_dict)
        """


if __name__ == "__main__":
    unittest.main()