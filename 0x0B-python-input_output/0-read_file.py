#!/usr/bin/python3
"""This module here defines a text file reading function"""


def read_file(filename=''):
    """Prints the contents of the UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
       print(f.read(), end="")
