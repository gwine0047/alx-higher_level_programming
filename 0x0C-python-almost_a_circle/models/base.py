#!/usr/bin/python3
"""This module depicts a class Base"""


class Base:
    """Class  Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects