#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class that defines a square with attribute"""

    def __init__(self, size=0):
        """
        Initializes the square

        Attributes:
            size (int): the size of a side of a square
        Raises:
            TypeError: size is not a int
            ValueError: size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
