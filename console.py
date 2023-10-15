#!/usr/bin/python3
"""
HBNBCommand class.
"""
import cmd


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
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        
        class_to_create = models.classes.get(class_name)
        if class_to_create:
            new_instance = class_to_create()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
