#!/usr/bin/python3
""" Module for the Base class"""
import json


class Base:
    """The “base” of all other classes it manages id attribute
    in all classes and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"

        list_dictionaries = []
        if list_objs is not None:
            for object in list_objs:
                list_dictionaries.append(object.to_dictionary())
        JSON_string = Base.to_json_string(list_dictionaries)
        with open(file_name, "w") as f:
            f.write(JSON_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(0, 0)
        dummy.update(**dictionary)
        return dummy
