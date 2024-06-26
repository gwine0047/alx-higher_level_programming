#!/usr/bin/python3
"""This is a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Writes a string to a UTF8 text."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
