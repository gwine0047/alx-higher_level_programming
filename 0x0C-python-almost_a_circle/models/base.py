#!/usr/bin/python3
"""This module depicts a class Base"""
import json
import csv
import turtle


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
        representation
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
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves python objs as csv"""
        filename = f"{cls.__name__}.json"

        with open(filename, "w") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads csv to python objs"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]

                # reading csv file.All in strings...
                # need to convert values to int
                dict_list = csv.DictReader(csv_file, fieldnames=field_names)
                new_dicts = []

                # iterating through the list and coverting key to int
                for d in dict_list:
                    converted_dict = {}
                    for key, value in d.items():
                        converted_dict[key] = int(value)

                    new_dicts.append(converted_dict)
                dict_list = new_dicts

                instance_list = []
                for d in dict_list:
                    instance_list.append(cls.create(**d))
                return instance_list
        except FileNotFoundError:
            return {}

    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all
        the Rectangles and Squares
        using the turtle module
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#FBAD00")
        turt.pensize(4)
        turt.shape("turtle")

        for r in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(r.x, r.y)
            turt.down()

            for _ in range(2):
                turt.forward(r.width)
                turt.left(90)
                turt.forward(r.height)
                turt.left(90)

            turt.hideturtle()

        for sq in list_squares:
            turt.color("#A52A2A")
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()

            for _ in range(4):
                turt.forward(sq.width)
                turt.left(90)

            turt.hideturtle()
        turtle.exitonclick()
