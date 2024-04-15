#!/usr/bin/python3
"""This is a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """To insert a text after each line with a given string"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
