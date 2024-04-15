#!/usr/bin/python3
"""This is a module with a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON format text file object"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
