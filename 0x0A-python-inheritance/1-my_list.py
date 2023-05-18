#!/usr/bin/python3
""" The module here inherits from the list class"""


class MyList(list):
   """ This class inherits from list"""
   def print_sorted(self):
       """ Prints a sorted list """
       print(sorted(self))
