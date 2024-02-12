#!/usr/bin/python3
"""
Module: user.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Represents a system user with email, password, first name, and last name.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new user.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the User class
    email = ""
    password = ""
    first_name = ""
    last_name = ""

