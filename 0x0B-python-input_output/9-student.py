#!/usr/bin/python3
"""This module here defines a class student"""


class Student:
    """This class represents a student"""

    def __init__(self, first_name, last_name, age):
        """This func initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the student"""
        return self.__dict__
