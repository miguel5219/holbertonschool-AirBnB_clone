#!/usr/bin/python3
"""module contains the class HBNBCommand"""

import cmd
import models.base_model
import models


class HBNBCommand(cmd.Cmd):
    """ class to implements a basic prompt to handle objects"""

    prompt = '(hbnb)'

    cls_id = {
        "BaseModel": "base_model"
    }

    def for_create(self, line):
        """ created a new instance of BaseModel """

        read_line = line.split(" ")
        if  read_line == ['']:
            print("** class name missing **")
        elif read_line[0] not in HBNBCommand.cls_id.keys():
            print("** class doesn't exist **")
        else:
            mod = HBNBCommand.cls_id[read_line[0]]
            b_1 = eval(
                f"models.{mod}.{read_line[0]}()")
            b_1.save()
            print(b_1.id)

    def for_show(self, line):

        read_line = line.split(" ")
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.cls_id.keys():
            print("** class does't exist **")
            return
        elif len(read_line) < 2:
            print("** instance id missing **")
            return

        conc = read_line[0] + "." + read_line[1]
        if not models.storage._FileStorage__objects.get(conc):
            print("** no instance found **")
        else:
            obj = models.storage._FileStorage__objects[conc]
            print(obj)

    def for_EOF(self, line):
        return True

    def for_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
