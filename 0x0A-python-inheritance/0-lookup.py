#!/usr/bin/python3
""" The module returns a list of available attributes and methids of an object"""


def lookup(obj):
    """ The function looks out for all attributes and methods of an object"""
    return dir(obj)
