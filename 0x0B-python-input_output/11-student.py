#!/usr/bin/python3
"""A module that defines a class Student"""


class Student:
    """Defining a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializing a new Instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This fetches a dict rep of the instance Student"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {each: getattr(self, each) for each in attrs if hasattr(self, each)}
        return self.__dict__

    def reload_from_json(self, json):
        """Function replaces attributes of Student"""
        for i, j in json.items():
            setattr(self, i, j)
