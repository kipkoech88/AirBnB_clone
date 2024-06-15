#!/usr/bin/python3
"""
AirBnB console
"""
import cmd
import sys
import os


class AirBnB(cmd.Cmd):
    """ AirBnB console """
    intro = ' Welcome to AirBnB console v1.0 '
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ' '

    def do_EOF(self, command):
        """ Terminate the console session """
        return True

    def help_EOF(self):
        """ help exit the program"""
        print("exit the program without formating\n")

    def do_quit(self, command):
        """ quit the console """
        exit()

    def help_quit(self):
        """ to end the session with formating
        use quit command
        """
        print("Exit the program with formating")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        AirBnB().onecmd(' '.join(sys.argv[1:]))
    else:
        AirBnB().cmdloop()
