#!/usr/bin/python3
"""
Module: review.py
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Represents a review of a place/house with text, user_id, and place_id attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new review.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the Review class
    text = ""
    user_id = ""
    place_id = ""
