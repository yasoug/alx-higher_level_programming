#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class that defines a square with attribute"""

    def __init__(self, size=0, position=(0,0)):
        """
        Initializes the square

        Attributes:
            size (int): the size of a side of a square
            position (int): 
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter : returns the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : set the position attribute"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance : that returns the square area"""
        return (self.__size)**2

    def my_print(self):
        """Public instance : that prints the square with # character"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
