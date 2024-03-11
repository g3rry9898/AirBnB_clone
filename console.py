#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """quiting the command prompt"""
        return True
    def do_quit(self, line):
        """quiting the console"""
        print("exiting prompt")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
