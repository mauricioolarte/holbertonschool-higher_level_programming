#!/usr/bin/python3
""" this document is for defining a rectangle"""


class Rectangle:
    """ this is a rectangle, simple class"""
    def __init__(self, width=0, height=0):
        if not type(width) is int:
            raise TypeError('width must be an integer')
        if not type(height) is int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if value is None:
            raise TypeError('width must be an integer')
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if value is None:
            raise TypeError('height must be an integer')
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
