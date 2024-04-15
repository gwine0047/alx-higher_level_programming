#!/usr/bin/python3
"""This is a module with a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """returns a python object"""
    with open(filename) as file:
        return json.loads(file)
