#!/usr/bin/python3
"""This is a module Write a script that adds all arguments to a Python list"""
import json


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        additions = load_from_json_file("add_item.json")
    except FileNotFoundError:
        additions = []
    additions.extend(sys.argv[1:])
    save_to_json_file(additions, "add_items.json")