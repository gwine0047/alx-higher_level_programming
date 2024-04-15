#!/usr/bin/python3
"""A module that defines a Python class-toJSON function"""


def class_to_json(obj):
    """Function returns a representation of a data structure"""
    return obj.__dict__
