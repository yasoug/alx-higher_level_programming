#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Square; inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter : size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter : size (width and height)"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """prints [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)
