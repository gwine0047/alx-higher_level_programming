#!/usr/bin/python3
"""a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False"""


def inherits_from(obj, a_class):
    """Returns true if directly or indirectly
    inheriting from a_class"""

    return type(obj) != a_class and isinstance(obj, a_class)
