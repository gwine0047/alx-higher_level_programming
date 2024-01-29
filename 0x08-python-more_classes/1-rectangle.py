#!/usr/bin/python3
"""A rectangle defining class"""

class Rectangle:
    """This is everything about the rectangle"""
    def __init__(self, width, height):
        """
        Initializing the rectangle class:
            Args:
                width: width of the rectangle.
                height: height of the rectangle.
            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width attribute retrieval"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height attribute retrieval"""
        return self.__height

    @height.setter
    def height(self, value):
        """height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value   


