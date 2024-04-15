#!/usr/bin/python3
"""A module that defines a class Student"""


class Student:
    """Defining a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializing a new Instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This fetches a dict rep of the instance Student"""
        return self.__dict__
