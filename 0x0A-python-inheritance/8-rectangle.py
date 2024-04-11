#!/usr/bin/python3
"""This module inherits from a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle and inherits from the
    class BaseGeometry"""

    def __init__(self, width, height):
        """Initializtion of a new Rectangle"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
