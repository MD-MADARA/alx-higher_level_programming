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
