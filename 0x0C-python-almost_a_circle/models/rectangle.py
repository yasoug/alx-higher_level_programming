#!/usr/bin/python3
"""class  Rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines class Rectangle; inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
