#!/usr/bin/python3
"""AirBnb Clone Console Module"""
from cgi import parse
import cmd
import sys
import json
import os
import re
from shlex import split
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define HBNB console"""

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User,
               'City': City, 'Place': Place,
               'Amenity': Amenity, 'Review': Review, 'State': State}

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def emptyline(self):
        """Does nothing."""
        pass

    def create(self, arg):
        """Creates a new instance that's inherited from BaseModel."""
        if len(arg) == 0:
            print("** class name missing **")
            return

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        new_line = None
        if arg:
            arg_line = arg.split()
            if len(arg_line) == 1:
                if arg in self.classes.keys():
                    new_line = self.classes[arg]()
                    new_line.save()
                    print(new_line.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split(" ")[0] == "":
            print("** class name missing **")
            return
        elif arg.split(" ")[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1 and arg.split(" ")[1] != "":
            key = arg.split(" ")[0] + '.' + arg.split(" ")[1]
            if key in storage.all():
                all_ = storage.all()
                print(all_[key])
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if len(arg) == 0 or arg.split(" ")[0] == "":
            print("** class name missing **")
            return
        arg_list = arg.split(" ")
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if arg_list[1] == "":
                print('** instance id missing **')
                return
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
