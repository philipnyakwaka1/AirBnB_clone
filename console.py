#!/usr/bin/python3
"""
HBNBCommand class.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review,
               "User": User, }

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
        """
        - Creates new instance of BaseModel and
        - saves it to the JSON file
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string rep of an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string rep of instances based or not on the class name"""
        args = arg.split()
        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(instance) for instance in
                  storage.all(class_name).values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id...
        ...by adding or updating an attribute
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    instance = instances[key]
                    try:
                        att_type = type(getattr(instance, attribute_name))
                        setattr(instance, attribute_name,
                                att_type(attribute_value))
                        instance.save()
                    except AttributeError:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieves the number of instances of a specified class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            count = len(storage.all(class_name))
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
