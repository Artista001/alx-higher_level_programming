#!/usr/bin/python3
"""This module here defines a python class to JSON function"""


def class_to_json(obj):
    """This returns the dictionary rep of a simple data structure"""
    return obj.__dict__
