#!/usr/bin/python3
import cmd


class test_cmd(cmd.Cmd):
    SIBLINGS = ["Sally", "Josephine", "Freddy", "Philip"]

    def preloop(self):
        print("Entering cmd")

    def do_greet(self, line):
        """Greets the user"""
        print(f"hello {line}")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.SIBLINGS[:]
        else:
            completions = [s for s in self.SIBLINGS if s.startswith(text)]
        return completions

    def do_EOF(self, line):
        print("EOF detected")
        return True

    def postloop(self):
        print("Exited cmd")

    def parseline(self, line):
        print('parseline({!r}) =>'.format(line), end='')
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret


if __name__ == '__main__':
    test_cmd().cmdloop()
