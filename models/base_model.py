#!/usr/bin/python3
"""Establishes the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Embodies the BaseModel for the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Set up a new instance of the BaseModel.

        Args:
            *args (any): Not utilized.
            **kwargs (dict): Pairs of keys and values representing attributes..
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Refresh the 'updated_at' field with the current date and time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Retrieve the dictionary representation of the BaseModel instance..

        Incorporates the key/value pair 'class' that represents
        the name of the object's class..
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Provide the printable or string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
