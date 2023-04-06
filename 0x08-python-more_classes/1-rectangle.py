#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
   """this represents a rectangle"""

   def __init__(self, width=0, height=0):
       """Initializing the rectangle class
       Args:
           width: Represents the width of the rectangle
           height: Represents the height of the rectangle
       Raises:
             TypeError: if size is not an integer
             ValueError: if size is less than zero
       """

       self.width = width
       self.height = height


   @property
   def width(self):
       """retrieves the width attribute"""
       return self.__width


   @width.setter
   def width(self, value):
       """sets the width attribute"""
       if not isinstance(value, int):
           raise TypeError("Width must be an integer")
       if value < 0:
           raise ValueError("Width must be >= 0")
       sels.__width = value
