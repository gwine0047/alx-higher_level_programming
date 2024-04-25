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
        # Constructor of the parent class
        super().__init__(id)

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
        for a in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overriding the __str__ method"""

        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 3:
                    self.x = arg
                elif num == 2:
                    self.height = arg
                elif num == 4:
                    self.y = arg
                else:
                    continue
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break
        # if args:
        #     attributes = {"id", "width", "height", "x", "y"}
        #     for index, value in enumerate(attributes):
        #         if index < len(args):
        #             setattr(self, value, args[index])

    def to_dictionary(self):
        """returns a dixtionary rep of Rectangle"""
        dic_rec = {
            "id":self.id,
            "width":self.width,
            "height":self.height,
            "x":self.x,
            "y":self.y
        }
        return (dic_rec)