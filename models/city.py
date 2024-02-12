#!/usr/bin/python3
"""
Module: city.py
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Represents a city with various attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new city.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the City class
    name = ""
    state_id = ""

