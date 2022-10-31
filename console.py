#!/usr/bin/python3
"""module contains the class HBNBCommand"""

import cmd
import models.base_model
import models


class HBNBCommand(cmd.Cmd):
    """ class to implements a basic prompt to handle objects"""

    def do_EOF(self, line):
        return True

    def do_quit(self, hbnb):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
