#!/usr/bin/python3

import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


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
        state1 = State()
        state3 = State("hello", "wait", "in")

        key = f"{type(state1).__name__}.{state1.id}"

        self.assertIsInstance(state1.name, str)
        self.assertEqual(state3.name, "")
        state1.name = "Chicago"
        self.assertEqual(state1.name, "Chicago")
        self.assertIn(key, storage.all())

    def test_state_initialization(self):
        """Test public instances during initialization."""
        state1 = State()
        state2 = State(**state1.to_dict())

        self.assertIsInstance(state1.id, str)
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)
        self.assertEqual(state1.updated_at, state2.updated_at)

    def test_state_string_representation(self):
        """Test string representation."""
        state1 = State()
        expected_str = f"[{type(state1).__name__}] ({state1.id}) {state1.__dict__}"
        self.assertEqual(state1.__str__(), expected_str)

    def test_state_save_method(self):
        """Test save method."""
        state1 = State()
        old_updated_at = state1.updated_at
        state1.save()
        self.assertNotEqual(state1.updated_at, old_updated_at)

    def test_state_to_dict_method(self):
        """Test to_dict method."""
        state1 = State()
        state2 = State(**state1.to_dict())

        dict_representation = state2.to_dict()

        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(
            dict_representation['__class__'], type(state2).__name__)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertNotEqual(state1, state2)


if __name__ == "__main__":
    unittest.main()
