#!/usr/bin/python3
""" Module for the Base class"""
import json
import csv


class Base:
    """The “base” of all other classes it manages id attribute
    in all classes and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Instanes to file """
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
        """ JSON string to dictionary """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """
        dummy = cls(1) if cls.__name__ == "Square" else cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ File to instances """
        file_name = cls.__name__ + ".json"
        list_instances = []
        try:
            with open(file_name) as f:
                JSON_string = f.read()
            list_dicionaries = Base.from_json_string(JSON_string)
            for dictionary in list_dicionaries:
                list_instances.append(cls.create(**dictionary))

        except FileNotFoundError:
            pass
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        file_name = f"{cls.__name__}.csv"
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        ''' Csv file to object list '''
        file_name = f"{cls.__name__}.csv"
        list_objects = []
        with open(file_name, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(value) for value in row]
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": row[0], "width": row[1],
                                  "height": row[2], "x": row[3], "y": row[4]}
                else:
                    dictionary = {"id": row[0], "size": row[1],
                                  "x": row[2], "y": row[3]}
                list_objects.append(cls.create(**dictionary))
        return list_objects
