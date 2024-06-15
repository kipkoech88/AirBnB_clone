#!/usr/bin/python3
"""
AirBnB console
"""
import cmd
import sys


class AirBnB(cmd.Cmd):
    """ AirBnB console """
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
        """ exit with formating"""
        print("Exit the program with formating")


if __name__ == "__main__":
    AirBnB().cmdloop()
