#!/usr/bin/python3
"""
Defines unittests for the console.py module.
Unittest classes:
    TestConsole
"""

import unittest
import os
import sys
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Unittests for the console.py module."""

    def setUp(self):
        """Set up test environment."""
        self.console_stdout = StringIO()
        self.console_stderr = StringIO()
        sys.stdout = self.console_stdout
        sys.stderr = self.console_stderr

    def tearDown(self):
        """Tear down test environment."""
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        del self.console_stdout
        del self.console_stderr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        """Test the create command."""
        commands = ['create BaseModel', 'create User', 'create State',
                    'create City', 'create Amenity', 'create Place',
                    'create Review']

        for command in commands:
            with self.subTest(command=command):
                HBNBCommand().onecmd(command)
                output = self.console_stdout.getvalue().strip()
                self.assertIn("created", output)

    def test_show(self):
        """Test the show command."""
        HBNBCommand().onecmd('create BaseModel')
        output = self.console_stdout.getvalue().strip()
        model_id = output.split()[-1]

        commands = ['show BaseModel', 'show User', 'show State',
                    'show City', 'show Amenity', 'show Place',
                    'show Review']

        for command in commands:
            with self.subTest(command=command):
                HBNBCommand().onecmd(command + ' ' + model_id)
                output = self.console_stdout.getvalue().strip()
                self.assertIn("BaseModel", output)

    def test_destroy(self):
        """Test the destroy command."""
        HBNBCommand().onecmd('create BaseModel')
        output = self.console_stdout.getvalue().strip()
        model_id = output.split()[-1]

        commands = ['destroy BaseModel', 'destroy User', 'destroy State',
                    'destroy City', 'destroy Amenity', 'destroy Place',
                    'destroy Review']

        for command in commands:
            with self.subTest(command=command):
                HBNBCommand().onecmd(command + ' ' + model_id)
                output = self.console_stdout.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_all(self):
        """Test the all command."""
        HBNBCommand().onecmd('create BaseModel')
        output = self.console_stdout.getvalue().strip()

        commands = ['all BaseModel', 'all User', 'all State',
                    'all City', 'all Amenity', 'all Place',
                    'all Review']

        for command in commands:
            with self.subTest(command=command):
                HBNBCommand().onecmd(command)
                output = self.console_stdout.getvalue().strip()
                self.assertIn("BaseModel", output)

    def test_update(self):
        """Test the update command."""
        HBNBCommand().onecmd('create BaseModel')
        output = self.console_stdout.getvalue().strip()
        model_id = output.split()[-1]

        commands = ['update BaseModel {} name "NewName"'.format(model_id),
                    'update BaseModel {} number 42'.format(model_id),
                    'update BaseModel {} is_valid True'.format(model_id)]

        for command in commands:
            with self.subTest(command=command):
                HBNBCommand().onecmd(command)
                obj = BaseModel()
                obj.reload()
                self.assertEqual(obj.name, "NewName")
                self.assertEqual(obj.number, 42)
                self.assertTrue(obj.is_valid)


if __name__ == "__main__":
    unittest.main()
