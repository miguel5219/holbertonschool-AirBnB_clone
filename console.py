#!/usr/bin/python3
"""module contains the class HBNBCommand"""

import cmd
import models.base_model
import models


class HBNBCommand(cmd.Cmd):
    """ class to implements a basic prompt to handle objects"""

    prompt = '(hbnb) '

    class_id = {
        "BaseModel": "base_model"
    }

    def do_create(self, line):
        """ created a new instance of BaseModel """

        read_line = line.split(" ")
        if  read_line == ['']:
            print("** class name missing **")
        elif read_line[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
        else:
            mod = HBNBCommand.class_id[read_line[0]]
            b_1 = eval(
                f"models.{mod}.{read_line[0]}()")
            b_1.save()
            print(b_1.id)

    def do_show(self, line):

        read_line = line.split(" ")
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.class_id.keys():
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

    def do_destroy(self, line):

        read_line = line.split(" ")
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(read_line) < 2:
            print("** instance id missing **")
            return

        conc = read_line[0] + "." + read_line[1]
        if not models.storage._FileStorage__objects.get(conc):
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[conc]
            models.storage.save()

    def do_all(self, line):

        read_line = line.split(" ")
        if read_line[0] not in [*HBNBCommand.class_id.keys(), '']:
            print("** class doesn't exist **")
        else:
            list_print = []
            for value in models.storage._FileStorage__objects.values():
                if (value.__class__.__name__ == read_line[0] or
                        read_line == ['']):
                    list_print.append(str(value))
            print(list_print)

    def do_update(self, line):

        read_line = line.split(' ')
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(read_line) < 2:
            print("** instance id missing **")
            return

        conc = read_line[0] + "." + read_line[1]
        if not models.storage._FileStorage__objects.get(conc):
            print("** no instance found **")
        elif len(read_line) < 3:
            print("** attribute name missing **")
        elif len(read_line) < 4:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[conc]
            setattr(obj, read_line[2], eval(read_line[3]))

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
