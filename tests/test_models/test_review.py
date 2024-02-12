#!/usr/bin/python3
"""
Unit tests for the `Review` module.
"""
import os
import unittest
from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReviewClass(unittest.TestCase):
    """Test cases for the `Review` class."""

    def setUp(self):
        # Any setup code goes here (if needed)
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_review_attributes(self):
        """Test class attributes."""
        review1 = Review()
        review2 = Review("hello", "wait", "in")

        self.assertIsInstance(review1.text, str)
        self.assertIsInstance(review1.user_id, str)
        self.assertIsInstance(review1.place_id, str)
        self.assertEqual(review2.text, "")

    def test_review_initialization(self):
        """Test public instances during initialization."""
        review1 = Review()
        review2 = Review(**review1.to_dict())

        self.assertIsInstance(review1.id, str)
        self.assertIsInstance(review1.created_at, datetime)
        self.assertIsInstance(review1.updated_at, datetime)
        self.assertEqual(review1.updated_at, review2.updated_at)

    def test_review_string_representation(self):
        """Test string representation."""
        review1 = Review()
        expected_str = f"[{type(review1).__name__}] ({review1.id}) {review1.__dict__}"
        self.assertEqual(review1.__str__(), expected_str)

    def test_review_save_method(self):
        """Test save method."""
        review1 = Review()
        old_updated_at = review1.updated_at
        review1.save()
        self.assertNotEqual(review1.updated_at, old_updated_at)

    def test_review_to_dict_method(self):
        """Test to_dict method."""
        review1 = Review()
        review2 = Review(**review1.to_dict())

        dict_representation = review2.to_dict()

        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(
            dict_representation['__class__'], type(review2).__name__)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertNotEqual(review1, review2)


if __name__ == "__main__":
    unittest.main()
