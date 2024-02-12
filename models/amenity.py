#!/usr/bin/python3
"""
Module: amenity.py
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Represents an amenity provided by a place/house.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new amenity.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the Amenity class
    name = ""
