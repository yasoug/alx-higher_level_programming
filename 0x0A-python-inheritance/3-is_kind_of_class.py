#!/usr/bin/python3
"""class checks if object is an instance of class that it inherited from"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the obj is an instance of, or if the object is an instance
    of a class that inherited from, the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
