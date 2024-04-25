#!/usr/bin/python3
"""This module depicts a class Base"""
import json

class Base:
    """Class  Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string 
        representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return"[]"
        to_json = json.dumps(list_dictionaries)
        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """
         class method that writes the 
         JSON string representation of 
         list_objs to a file
         """

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """
        returns the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all
        attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(2)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())

                instance_list = []
                for dictionary in list_dicts:
                    instance_list.append(cls.create(**dictionary))
                return instance_list
        except FileNotFoundErroe:
            return []
