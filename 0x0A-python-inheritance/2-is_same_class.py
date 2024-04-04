#!/usr/bin/python3
"""This module returns true for an instance of same specified class"""


def is_same_class(obj, a_class):
    """Returns an true if obj is an instance, otherwise False"""

    return (type(obj) == a_class)
