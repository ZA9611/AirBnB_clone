#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Review class."""
=======
"""Establishes the Review class."""
>>>>>>> c59caba2d83213f35a4ad96cc4b859e5a6def310
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
=======
    """Embodies a review..

    Attributes:
        place_id (str): The identification number for the Place..
        user_id (str): The identification number for the User.
        text (str): The content of the review.
>>>>>>> c59caba2d83213f35a4ad96cc4b859e5a6def310
    """

    place_id = ""
    user_id = ""
    text = ""
