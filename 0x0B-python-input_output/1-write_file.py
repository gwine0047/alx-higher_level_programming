#!/usr/bin/python3
"""This is a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
