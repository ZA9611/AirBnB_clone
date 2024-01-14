#!/usr/bin/python3
"""Establishes the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curlyBraces = re.search(r"\{(.*?)\}", arg)
    b = re.search(r"\[(.*?)\]", arg)
    if curlyBraces is None:
        if b is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lx = split(arg[:b.span()[0]])
            retLength = [i.strip(",") for i in lx]
            retLength.append(b.group())
            return retLength
    else:
        lx = split(arg[:curlyBraces.span()[0]])
        retLength = [i.strip(",") for i in lx]
        retLength.append(curlyBraces.group())
        return retLength


class HBNBCommand(cmd.Cmd):
    """Establishes the cmd interpreter for HolbertonBnB..

    Attributes:
        prompt (str): "The cmd input interface..
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """No action is taken when an empty line is received."""
        pass

    def default(self, arg):
        """The standard behavior of the cmd module when the input is invalid."""
        argDictionary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        matcher = re.search(r"\.", arg)
        if matcher is not None:
            argumentL = [arg[:matcher.span()[0]], arg[matcher.span()[1]:]]
            matcher = re.search(r"\((.*?)\)", argumentL[1])
            if matcher is not None:
                cmd = [argumentL[1][:matcher.span()[0]], matcher.group()[1:-1]]
                if cmd[0] in argDictionary.keys():
                    call = "{} {}".format(argumentL[0], cmd[1])
                    return argDictionary[cmd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit cmd to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argumentL = parse(arg)
        if len(argumentL) == 0:
            print("** class name missing **")
        elif argumentL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argumentL[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argumentL = parse(arg)
        objDictionary = storage.all()
        if len(argumentL) == 0:
            print("** class name missing **")
        elif argumentL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argumentL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argumentL[0], argumentL[1]) not in objDictionary:
            print("** no instance found **")
        else:
            print(objDictionary["{}.{}".format(argumentL[0], argumentL[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argumentL = parse(arg)
        objDictionary = storage.all()
        if len(argumentL) == 0:
            print("** class name missing **")
        elif argumentL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argumentL) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argumentL[0], argumentL[1]) not in objDictionary.keys():
            print("** no instance found **")
        else:
            del objDictionary["{}.{}".format(argumentL[0], argumentL[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, display string representations of all instantiated objects."""
        argumentL = parse(arg)
        if len(argumentL) > 0 and argumentL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectL = []
            for object in storage.all().values():
                if len(argumentL) > 0 and argumentL[0] == object.__class__.__name__:
                    objectL.append(object.__str__())
                elif len(argumentL) == 0:
                    objectL.append(object.__str__())
            print(objectL)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argumentL = parse(arg)
        count = 0
        for object in storage.all().values():
            if argumentL[0] == object.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating 
        a given attribute key/value pair or dictionary."""
        argumentL = parse(arg)
        objDictionary = storage.all()

        if len(argumentL) == 0:
            print("** class name missing **")
            return False
        if argumentL[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argumentL) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argumentL[0], argumentL[1]) not in objDictionary.keys():
            print("** no instance found **")
            return False
        if len(argumentL) == 2:
            print("** attribute name missing **")
            return False
        if len(argumentL) == 3:
            try:
                type(eval(argumentL[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argumentL) == 4:
            object = objDictionary["{}.{}".format(argumentL[0], argumentL[1])]
            if argumentL[2] in object.__class__.__dict__.keys():
                valueType = type(object.__class__.__dict__[argumentL[2]])
                object.__dict__[argumentL[2]] = valueType(argumentL[3])
            else:
                object.__dict__[argumentL[2]] = argumentL[3]
        elif type(eval(argumentL[2])) == dict:
            object = objDictionary["{}.{}".format(argumentL[0], argumentL[1])]
            for k, v in eval(argumentL[2]).items():
                if (k in object.__class__.__dict__.keys() and
                        type(object.__class__.__dict__[k]) in {str, int, float}):
                    valueType = type(object.__class__.__dict__[k])
                    object.__dict__[k] = valueType(v)
                else:
                    object.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
