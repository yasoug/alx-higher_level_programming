#!/usr/bin/python3
"""class with no class or object attribute"""


class LockedClass:
    """
    it prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called "first_name"
    """
    __slots__ = "first_name"
