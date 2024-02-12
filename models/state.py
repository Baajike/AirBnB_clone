#!/usr/bin/python3
"""
Module: state.py
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Represents a state in the application with a name attribute.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new state.
        If kwargs is provided, sets attributes from a dictionary.
        If not, generates new attributes and adds the instance to storage.
        """
        super().__init__(*args, **kwargs)

    # Additional attributes specific to the State class
    name = ""

