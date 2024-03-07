#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import json
import os
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define HBNB console"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
