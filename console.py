#!/usr/bin/python3
"""
HBNBCommand class.
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Exit program when EOF is encoured (ctrl+D)"""
        return True

    def emptyline(self):
        """Empty line should not print anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        valid_cls = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

        if class_name not in valid_cls:
            print("** class doesn't exist **")
            return

        class_to_create = HBNBCommand.classes.get(class_name)
        if class_to_create:
            new_instance = class_to_create()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints string rep of an instance by class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance by class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all instances or all instances by class name"""
        args = args.split()
        if not args:
            instances = storage.all()
            for instance in instances.values():
                print(instance)
        else:
            class_name = args[0]
            if class_name in ("BaseModel",):
                instances = storage.all(class_name)
                for instance in instances.values():
                    print(instance)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key in all_instances:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            value = args[3]
            setattr(all_instances[key], attribute_name, value)
            all_instances[key].save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
