#!/usr/bin/python3
"""
file_storage.py

Defines the `FileStorage` class for serialization and deserialization.
"""
import os
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    Handles serialization to and deserialization from a JSON file.
    """

    # Path to the JSON file
    __file_path = "file.json"
    # Dictionary to store objects by <class name>.id
    __objects = {}

    def all(self):
        """
        Retrieves the stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the stored objects.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and writes the objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as file:
            serialized_objects = {k: v.to_dict()
                                  for k, v in FileStorage.__objects.items()}
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes and loads objects from the JSON file.
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    deserialized_objects = json.load(file)
                except json.JSONDecodeError:
                    return

                FileStorage.__objects = {
                    k: current_classes[k.split('.')[0]](**v)
                    for k, v in deserialized_objects.items()}
