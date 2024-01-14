#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
=======
"""Establishes the User class."""
>>>>>>> c59caba2d83213f35a4ad96cc4b859e5a6def310
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
=======
    """Establishes the User class.

    Attributes:
        email (str): The email address of the user.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
>>>>>>> c59caba2d83213f35a4ad96cc4b859e5a6def310
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
