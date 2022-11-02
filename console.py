#!/usr/bin/python3
"""module contains the class HBNBCommand"""

import cmd
import models.base_model
import models
import re


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

    def for_destroy(self, line):

        read_line = line.split(" ")
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.cls_id.keys():
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

    def for_all(self, line):

        read_line = line.split(" ")
        if read_line[0] not in [*HBNBCommand.cls_id.keys(), '']:
            print("** class doesn'texist **")
        else:
            list_print = []
            for val in models.storage._FileStorage__objects.values():
                if (val.__class__.__name__ == read_line[0] or
                        read_line == ['']):
                    list_print.append(str(val))
            print(list_print)

    def for_update(self, line):

        read_line = line.split(' ')
        if read_line == ['']:
            print("** class name missing **")
            return
        elif read_line[0] not in HBNBCommand.cls_id.keys():
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

    def default(self, *args):
        args_splitted = args[0].split('.')
        if len(args_splitted) < 2:
            print("** incorrect command **")
            return

        if args_splitted[1] == "all()":
            self.for_all(f'{args_splitted[0]}')
        elif args_splitted[1] == "count()":

            clss = models.storage._FileStorage__objects.items()
            print(len([k for k, v in clss
                       if v.__class__.__name__ == args_splitted[0]]))
        elif re.search("show()",args_splitted[1]):
            obj_id = args_splitted[1].replace("show(", "")[:-1]
            self.for_show(args_splitted[0] + " " + obj_id)

        elif re.search("destroy()", args_splitted[1]):
            obj_id = args_splitted[1].replace("destroy(", "")[:-1]
            self.for_destroy(args_splitted[0] + " " + obj_id)
        elif re.search("update()", args_splitted[1]):
            obj_args = args_splitted[1].replace("update(", "")[:-1]
            args = obj_args.split(", ", 1)

            if len(args) < 2:
                print("** usage: <class name>.update(<id>,"
                      " <attribute name>, <attribute value>)")
            elif "{" in args[1] and "}" in args[1] and ":" in args[1]:
                dic_args = eval(args[1])
                for key, value in dic_args.items():
                    if type(value) is str:
                        a = f"{args_splitted[0]} {args[0]} {key} \"{value}\""
                    else:
                        a = f"{args_splitted[0]} {args[0]} {key} {value}"
                    self.for_update(a)
            else:
                obj_args = obj_args.replace(",", "")
                self.for_update(args_splitted[0] + " " + obj_args)

    def for_EOF(self, line):
        return True

    def for_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
