#!/usr/bin/python3
"""This is a module the defines a function that returns a json string"""
import json


def from_json_string(my_str):
    """Function returns the Python rep of a JSON string"""
    return json.loads(my_str)
