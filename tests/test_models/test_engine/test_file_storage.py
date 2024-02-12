#!/usr/bin/python3
"""
Defining unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Test cases for FileStorage class instantiation."""

    def test_file_storage_instantiation_no_args(self):
        """Test instantiation of FileStorage with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_storage_instantiation_with_arg(self):
        """Test instantiation of FileStorage with an argument."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_file_path_is_private_str(self):
        """Test the privacy and type of __file_path attribute."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_objects_is_private_dict(self):
        """Test the privacy and type of __objects attribute."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test that the storage instance initializes correctly."""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Test cases for methods of the FileStorage class."""

    def setUp(self):
        pass

    def tearDown(self):
        """Reset FileStorage data after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all method of FileStorage."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Test all method with an argument."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test the new method of FileStorage."""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        """Test new method with additional arguments."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_none(self):
        """Test new method with None as an argument."""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test the save method of FileStorage."""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        """Test save method with an argument."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Test the reload method of FileStorage."""
        bm

