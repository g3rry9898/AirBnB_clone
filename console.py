#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """quiting the command prompt"""
        return True
    def do_quit(self, arg):
        """quiting the console"""

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
