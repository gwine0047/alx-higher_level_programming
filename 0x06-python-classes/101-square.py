#!/usr/bin/python3
""""Square module"""


class Square:
    """Declaring a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the fields of Square\
        Args:
            size: size of sqaure.
            position: position of square    
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Allot the size"""
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Allot the position"""
        return self.__position
    @position.setter
    def position(self, value):
        if value is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[1] < 0 or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
 
    def area(self):
        x = self.__size
        return x ** 2
    
    def my_print(self):
        """prints a square using '#'"""
        x = self.__size
        a,b = self.__position
        if x == 0:
            print("")
            return

        [print("") for i in range(0, b)]
        for i in range(0, x):
            [print(" ", end="") for j in range(0, a)]
            [print("#", end="") for k in range(0, x)]
            print("")

        def __str__(self):
            """Represent the print() form of square"""
            if self.__size != 0:
                [print("") for i in range(0, b)]
            for i in range(0, x):
                [print(" ", end="") for j in range(0, a)]
                [print("#", end="") for k in range(0, x)]
            if i != x - 1:
                print("")
            return ("")
