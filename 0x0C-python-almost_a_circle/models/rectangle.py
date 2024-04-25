#!/usr/bin/python3
"""This module defines a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """defining the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the attributes of Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id) #constructor of the parent class

    # All getter functions (encapsulation)
    @property
    def width(self):
        """Fetches the value for the width"""
        return self.__width

    @property
    def height(self):
        """Fetches the value for the height"""
        return self.__height

    @property
    def x(self):
        """Fetches the value for the x"""
        return self.__x

    @property
    def y(self):
        """Fetches the value for the y"""
        return self.__y

    # All setter functions
    @width.setter
    def width(self, value):
        """width setter"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x value setter"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y value setter"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the area using #"""
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """overriding the __str__ method"""

        return(f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")