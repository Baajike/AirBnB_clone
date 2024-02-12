#!/usr/bin/python3
"""
Module: place.py
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Represents a place/house with various attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new place.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the Place class
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
