#!/usr/bin/python3
"""This is a square module"""


class Square:
    """square class declaration"""
    def __init__(self, size=0):
        """class attributes initialization
        Args:
            size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
