#!/usr/bin/python3
"""This is a module the defines a function that changes a string-to-JSON"""
import json


def to_json_string(my_ob):
    """This functions returns a json rep of a string"""
    return json.dumps(my_ob)