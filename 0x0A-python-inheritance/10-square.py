#!/usr/bin/python3
"""
parent class BaseGeometry
subclass Rectangle
subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry"""
    def __init__(self, size):
        """initializes size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
