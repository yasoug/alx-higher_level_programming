#!/usr/bin/python3
"""class Base"""
import json
import csv


class Base:
    """will be the base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise new Base"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_inst = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                list_inst.append(cls.create(**instances[i]))
        except FileNotFoundError:
            pass
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        if list_objs is None:
            return []
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if cls.__name__ == "Rectangle":
                names = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                names = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=names)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of classes instantiated from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
