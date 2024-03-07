#!/usr/bin/python3
"""A rectangle defining class"""

class Rectangle:
    """This is everything about the rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
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

    def area(self):
        """It returns the area of the class Rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """It returns the perimeter of the class Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return(2*(self.__width +  self.__height))

    def __str__(self)-> str:
        """presents the defined rectangle with diagrams"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    rec += str(self.print_symbol)
                except Exception:
                    rec += type(self).print_symbol
            if i < self.__height - 1:
                rec += "\n"
        return (rec)

    def __repr__(self):
        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectange")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectange")
        if rect_2.area() >= rect_1.area():
            return rect_2
        else:
            return rect_1
        

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)