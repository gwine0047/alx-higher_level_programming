#!/usr/bin/python3
"""This is a function that reads a text file"""

def read_file(filename=""):
    """the content of a UTF-8 text file is printed"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")