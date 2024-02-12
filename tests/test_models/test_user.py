#!/usr/bin/python3
import os
import unittest
from datetime import datetime
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestStateClass(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        # Any setup code goes here (if needed)
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_state_attributes(self):
        """Test class attributes."""
        user1 = User()
        key = f"{type(user1).__name__}.{user1.id}"

        self.assertIn(key, storage.all())
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.password, str)
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)

    def test_state_initialization(self):
        """Test public instances during initialization."""
        user1 = User()
        user2 = User(**user1.to_dict())

        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime)
        self.assertIsInstance(user1.updated_at, datetime)
        self.assertEqual(user1.updated_at, user2.updated_at)

    def test_state_string_representation(self):
        """Test string representation."""
        user1 = User()
        expected_str = f"[{type(user1).__name__}] ({user1.id}) {user1.__dict__}"
        self.assertEqual(user1.__str__(), expected_str)

    def test_state_save_method(self):
        """Test save method."""
        user1 = User()
        old_updated_at = user1.updated_at
        user1.save()
        self.assertNotEqual(user1.updated_at, old_updated_at)

    def test_state_to_dict_method(self):
        """Test to_dict method."""
        user1 = User()
        user2 = User(**user1.to_dict())

        dict_representation = user2.to_dict()

        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(
            dict_representation['__class__'], type(user2).__name__)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertNotEqual(user1, user2)


if __name__ == "__main__":
    unittest.main()
