#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
=======
    """Embodies a place..

    Attributes:
        city_id (str): The identification number for the City..
        user_id (str): The identification number for the User.
        name (str): The specified name for the place.
        description (str): The detailed description of the place.
        number_rooms (int): The total count of rooms in the place.
        number_bathrooms (int): The quantity of bathrooms in the place.
        max_guest (int): The maximum capacity for guests in the place.
        price_by_night (int): The nightly rate for staying at the place.
        latitude (float): The geographical latitude of the place.
        longitude (float): The geographical longitude of the place.
        amenity_ids (list): A list of Amenity identifiers.
>>>>>>> c59caba2d83213f35a4ad96cc4b859e5a6def310
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
