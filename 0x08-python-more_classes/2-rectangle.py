#!/usr/bin/python3
""" this document is for defining a rectangle"""


class Rectangle:
    """ this is a rectangle, simple class"""
    def __init__(self, width=0, height=0):
        if not type(width) is int or not type(height) is int:
            raise TypeError('width must be an integer')
        if height < 0 or width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height is 0 or self.width is 0:
            perimeter = 0
        else:
            perimeter = self.__height * 2 + self.__width * 2
        return (perimeter)


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

