#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class that defines a square with attribute"""

    def __init__(self, size=0):
        """
        Initializes the square

        Attributes:
            size (int): the size of a side of a square
        """
        self.size = size

    @property
    def size(self):
        """Getter : returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : set the size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance : that returns the square area"""
        return (self.__size)**2

    def __eq__(self, other):
        """Instances are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Instances are not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Instance greater than the other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Instance greater than or equals the other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Instance lesser than the other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Instance lesser than or equals the other"""
        return self.area() <= other.area()
