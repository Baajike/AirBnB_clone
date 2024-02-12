#!/usr/bin/python3
"""
Module: base_model.py
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class defining common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an object with its attributes.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        if kwargs:
            self.__set_attributes_from_dict(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __set_attributes_from_dict(self, attribute_dict):
        """
        Sets attributes from a dictionary.
        Converts 'created_at' and 'updated_at' strings to datetime objects.
        Ignores special keys like '__class__', 'created_at', and 'updated_at'.
        """
        for key, value in attribute_dict.items():
            if key not in ["__class__", "created_at", "updated_at"]:
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        Saves the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__.
        Also includes '__class__', 'created_at', and 'updated_at'.
        """
        obj_dict = {**self.__dict__}
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
