#!/usr/bin/ env python3
"""A subclass Square for the base class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialization of a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
