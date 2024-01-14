#!/usr/bin/python3
"""Establishes the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Embodies an abstract storage mechanism..

    Attributes:
        __file_path (str): The designated filename for saving objects.
        __objects (dict): A collection of created objects in a dictionary format.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Assign obj to __objects with the key formatted as <obj_class_name>.id."""
        objectClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objectClassName, obj.id)] = obj

    def save(self):
        """Convert __objects into JSON format and save to the file specified by __file_path."""
        oDictionary = FileStorage.__objects
        objectDictionary = {obj: oDictionary[obj].to_dict() for obj in oDictionary.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectDictionary, f)

    def reload(self):
        """If it exists, convert the JSON file specified by __file_path back into the __objects format."""
        try:
            with open(FileStorage.__file_path) as f:
                objectDictionary = json.load(f)
                for o in objectDictionary.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return
