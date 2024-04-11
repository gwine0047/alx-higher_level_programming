#!/usr/bin/python3
"""A module that inherits fron a class called list"""


class MyList(list):
    """Inhering from class list"""
    def print_sorted(self):
        """sorted list printing"""
        print(sorted(self))
