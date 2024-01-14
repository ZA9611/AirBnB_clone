#!/usr/bin/python3
"""Establishes the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Embodies an amenity..

    Attributes:
        name (str): The designated name for the amenity..
    """

    name = ""
