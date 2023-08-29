#!/usr/bin/python3
"""This is a square module"""


class Square:
    """square class declaration"""
    def __init__(self, size=0, position=(0, 0)):
        """
        class attributes initialization
        Args:
            size: size of square
            position: position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Attributes getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public method of class Square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the sqaure using '#'"""
        if self.__size == 0:
            print("")
        s = self.__size
        count = 0
        p1, p2 = self.__position
        for line in range(p2):
            print("")
        while count < s:
            a = 0
            while a < p1:
                print(" ", end='')
                a  = a + 1
            count2 = 0
            while count2 < s:
                print("{}".format("#"), end="")
                count2 += 1
            print("")
            count += 1