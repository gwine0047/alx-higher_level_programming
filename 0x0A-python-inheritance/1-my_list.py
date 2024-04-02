"""A module that inherits fron a class called list"""


class Mylist(list):
    """Inhering from class list"""
    def print_sorted(self):
        """sorted list printing"""
        print(sorted(self))