#!/usr/bin/python3
"""class  Rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines class Rectangle; inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter : width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter : width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter : height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter : x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter : x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter : y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter : y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle instance with the character #"""
        for i in range(self.__height):
            print(self.__width * "#")

    def __str__(self):
        """prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
