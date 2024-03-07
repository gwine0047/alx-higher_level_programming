#!/usr/bin/python3
""" A class that defines a rectangle"""


class Rectangle:
    """This is everything about the rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the traitis of this class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            """gets width features"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """sets width features"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        
        @property
        def height(self):
            """gets width features"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """sets height features"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """Return the rectangle's area"""
            return (self.__width * self.__height)
        
        def perimeter(self):
            """It returns the perimeter of the class Rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return(2*(self.__width +  self.__height))
        
        def __str__(self) -> str:
            """prints a diagram of the defined rectangle for an object"""
            if self.__width == 0 or self.__height == 0:
                return ("")
            rectangle = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += "#"
                if i < self.__height - 1:
                    rectangle += "\n"
            return (rectangle)

            def __repr_(self):
                """returns the rectangle's string representation"""
                return f"Rectangle ({self.__width}, {self.__height})"
            
            def __del__(self):
                """leaves a message for a deleted object/instance"""
                print("Bye rectangle...")
                Rectangle.number_of_instances -= 1
