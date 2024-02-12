#!/usr/bin/python3

import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class TestAmenityClass(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def setUp(self):
        """Set up any initial state needed for the tests."""
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_attributes(self):
        """Test method for class attributes."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        amenity3 = Amenity("hello", "wait", "in")

        key = f"{type(amenity1).__name__}.{amenity1.id}"
        self.assertIsInstance(amenity1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(amenity3.name, "")

    def test_amenity_initialization(self):
        """Test method for public instances."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        self.assertIsInstance(amenity1.id, str)
        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertIsInstance(amenity1.updated_at, datetime)
        self.assertEqual(amenity1.updated_at, amenity2.updated_at)

    def test_amenity_str_representation(self):
        """Test method for str representation."""
        amenity1 = Amenity()
        string = f"[{type(amenity1).__name__}] ({amenity1.id}) {amenity1.__dict__}"
        self.assertEqual(amenity1.__str__(), string)

    def test_amenity_save_method(self):
        """Test method for save."""
        amenity1 = Amenity()
        old_update = amenity1.updated_at
        amenity1.save()
        self.assertNotEqual(amenity1.updated_at, old_update)

    def test_amenity_to_dict_method(self):
        """Test method for to_dict."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        a_dict = amenity2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(amenity2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(amenity1, amenity2)


if __name__ == "__main__":
    unittest.main()

