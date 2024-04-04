#!/usr/bin/python3
"""A  class module named BaseGeometry"""


class BaseGeometry:
    """attributes and methods of te class"""

    def area(self):
        """a public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
