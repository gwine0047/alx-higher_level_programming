#!/usr/bin/python3
"""This is a square module"""


class Square:
    """square class declaration"""
    def __init__(self, size=0):
        """class attributes initialization
        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """Attributes getter"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public method of class Square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        count = self.__size
        while count > 0:
            print("#" * (self.__size))
            count -= 1
