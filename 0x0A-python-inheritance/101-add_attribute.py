#!/usr/bin/python3
"""A module that defines a function and adds attributes to objects"""


def add_attribute(obj, att, value):
    """Taking a new attribute from objects"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
    