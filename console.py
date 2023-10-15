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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
