#!/usr/bin/python3
"""class that returns list of object's attribute and methods"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))
