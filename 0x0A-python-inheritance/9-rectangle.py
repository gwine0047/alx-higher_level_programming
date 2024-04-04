#!/usr/bin/env python3
"""This module inherits from a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle and inherits from the
    class BaseGeometry"""

    def __init__(self, width, height):
        """Initializtion of a new Rectangle"""
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """area of rectangle is returned"""
        return self.__width * self.__height

    def __str__(self):
        """print() and str() representation of the rectangle is returned"""
        word = "[" + str(self.__class__.__name__) + "] "
        word += str(self.__width) + "/" + str(self.__height)
        return word
