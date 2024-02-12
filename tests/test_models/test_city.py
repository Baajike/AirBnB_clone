#!/usr/bin/python3
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

class TestCityClass(unittest.TestCase):
    """Test cases for the `City` class."""

    def setUp(self):
        """Set up any initial state needed for the tests."""
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_city_attributes(self):
        """Test method for class attributes."""
        city1 = City()
        city3 = City("hello", "wait", "in")

        key = f"{type(city1).__name__}.{city1.id}"

        self.assertIsInstance(city1.name, str)
        self.assertEqual(city3.name, "")
        city1.name = "Abuja"
        self.assertEqual(city1.name, "Abuja")

    def test_city_initialization(self):
        """Test method for public instances."""
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)
        self.assertEqual(city1.updated_at, city2.updated_at)

    def test_city_save_method(self):
        """Test save method."""
        old_update = city1.updated_at
        city1.save()
        self.assertNotEqual(city1.updated_at, old_update)

    def test_city_to_dict_method(self):
        """Test to_dict method."""
        a_dict = city2.to_dict()

        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(city2).__name__)
        self.assertIn('created_at', a_dict)
        self.assertIn('updated_at', a_dict)
        self.assertNotEqual(city1, city2)


if __name__ == "__main__":
    unittest.main()

