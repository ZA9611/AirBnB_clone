#!/usr/bin/python3
"""Establishes the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Embodies a state.

    Attributes:
        name (str): The designated name of the state..
    """

    name = ""
