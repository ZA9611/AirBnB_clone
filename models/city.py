#!/usr/bin/python3
"""Establishes the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Embodies a city.

    Attributes:
        state_id (str): The identifier for the state..
        name (str): The designated name of the city..
    """

    state_id = ""
    name = ""
