#!/usr/bin/python3
"""Establishes the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Embodies a review..

    Attributes:
        place_id (str): The identification number for the Place..
        user_id (str): The identification number for the User.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
