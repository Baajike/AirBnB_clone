#!/usr/bin/python3

""" Testing- base_model.py"""

import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test cases for the `BaseModel` class.
    """

    def setUp(self):
        """Set up any initial state needed for the tests."""
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_base_model_initialization_positive(self):
        """Test passing cases for `BaseModel` initialization."""
        base_model1 = BaseModel()
        base_model2_uuid = str(uuid.uuid4())
        base_model2 = BaseModel(id=base_model2_uuid, name="The Weeknd", album="Trilogy")
        self.assertIsInstance(base_model1.id, str)
        self.assertIsInstance(base_model2.id, str)
        self.assertEqual(base_model2_uuid, base_model2.id)
        self.assertEqual(base_model2.album, "Trilogy")
        self.assertEqual(base_model2.name, "The Weeknd")
        self.assertIsInstance(base_model1.created_at, datetime)
        self.assertIsInstance(base_model1.updated_at, datetime)
        self.assertEqual(str(type(base_model1)), "<class 'models.base_model.BaseModel'>")

    def test_to_dict_method(self):
        """Test method for to_dict."""
        base_model1 = BaseModel()
        base_model2_uuid = str(uuid.uuid4())
        base_model2 = BaseModel(id=base_model2_uuid, name="The Weeknd", album="Trilogy")
        base_model1_dict = base_model1.to_dict()
        self.assertIsInstance(base_model1_dict, dict)
        self.assertIn('id', base_model1_dict.keys())
        self.assertIn('created_at', base_model1_dict.keys())
        self.assertIn('updated_at', base_model1_dict.keys())
        self.assertEqual(base_model1_dict['__class__'], type(base_model1).__name__)
        with self.assertRaises(KeyError):
            base_model2.to_dict()

    def test_save_method(self):
        """Test method for save."""
        base_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base_model.save()
        time_difference = base_model.updated_at - date_now
        self.assertTrue(abs(time_difference.total_seconds()) < 0.01)

    def test_save_storage_method(self):
        """Tests that storage.save() is called from save()."""
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        data = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as file:
            self.assertEqual(len(file.read()), len(json.dumps(data)))
            file.seek(0)
            self.assertEqual(json.load(file), data)

    def test_save_method_no_args(self):
        """Tests save() with no arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_save_method_excess_args(self):
        """Tests save() with too many arguments."""
        self.reset_storage()
        with self.assertRaises(TypeError):
            BaseModel.save(self, 98)

    def test_str_representation_method(self):
        """Test method for str representation."""
        base_model1 = BaseModel()
        string = f"[{type(base_model1).__name__}] ({base_model1.id}) {base_model1.__dict__}"
        self.assertEqual(base_model1.__str__(), string)


if __name__ == "__main__":
    unittest.main()

