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
        self.__size = size

    @property
    def size(self):
        """Getter : returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : set the size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance : that returns the square area"""
        return (self.__size)**2

    def my_print(self):
        """Public instance : that prints the square with # character"""
        print("\n".join(["#" * self.__size for i in range(self.__size)]))
