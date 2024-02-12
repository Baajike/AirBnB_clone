#!/usr/bin/python3

import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
from datetime import datetime


class TestPlaceClass(unittest.TestCase):
    """Test cases for the `Place` class."""

    def setUp(self):
        # Any setup code goes here (if needed)
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_place_attributes(self):
        """Test class attributes."""
        place1 = Place()
        place3 = Place("hello", "wait", "in")

        key = f"{type(place1).__name__}.{place1.id}"

        self.assertIsInstance(place1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(place3.name, "")

        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.description, str)
        self.assertIsInstance(place1.number_bathrooms, int)
        self.assertIsInstance(place1.number_rooms, int)
        self.assertIsInstance(place1.price_by_night, int)
        self.assertIsInstance(place1.max_guest, int)
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.latitude, float)
        self.assertIsInstance(place1.amenity_ids, list)

    def test_place_initialization(self):
        """Test method for public instances."""
        place1 = Place()
        place2 = Place(**place1.to_dict())

        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
        self.assertEqual(place1.updated_at, place2.updated_at)

    def test_place_string_representation(self):
        """Test method for str representation."""
        place1 = Place()
        expected_str = f"[{type(place1).__name__}] ({place1.id}) {place1.__dict__}"
        self.assertEqual(place1.__str__(), expected_str)

    def test_place_save_method(self):
        """Test save method."""
        place1 = Place()
        old_updated_at = place1.updated_at
        place1.save()
        self.assertNotEqual(place1.updated_at, old_updated_at)

    def test_place_to_dict_method(self):
        """Test to_dict method."""
        place1 = Place()
        place2 = Place(**place1.to_dict())

        dict_representation = place2.to_dict()

        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(
            dict_representation['__class__'], type(place2).__name__)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertNotEqual(place1, place2)


if __name__ == "__main__":
    unittest.main()
