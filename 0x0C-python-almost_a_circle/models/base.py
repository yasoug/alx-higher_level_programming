#!/usr/bin/python3
"""class Base"""


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
