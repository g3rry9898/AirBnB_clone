import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        print("\nexiting")


    def do_empty_line(self, line):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
