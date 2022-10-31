#!/usr/bin/python3
"""module contains the class HBNBCommand"""

import cmd
import models.base_model
import models


class HBNBCommand(cmd.Cmd):
    """ class to implements a basic prompt to handle objects"""

    prompt = '(hbnb)'

    def for_EOF(self, line):
        return True

    def for_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
