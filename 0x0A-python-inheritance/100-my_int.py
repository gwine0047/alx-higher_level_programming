#!/usr/bin/python3
"""A module shows a class inheriting from the class Int"""


class MyInt(int):
    """using int operators == and !="""

    def __eq__(self, value):
        """substituting == with !="""
        return self.real != value

    def __ne__(self, value):
        """substituting != operator with =="""
        return self.real == value
