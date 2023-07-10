#!/usr/bin/python3
"""class checks if object is exactly an instance of class"""


def is_same_class(obj, a_class):
    """returns True if obj is exactly an instance of specified class"""
    return type(obj) == a_class
