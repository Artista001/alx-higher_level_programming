#!/usr/bin/python3
"""This module here defines a file-appending function"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
