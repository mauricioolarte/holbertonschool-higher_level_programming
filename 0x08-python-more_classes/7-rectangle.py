#!/usr/bin/python3
""" this document is for defining a rectangle"""


class Rectangle:
    """ this is a rectangle, simple class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not type(width) is int or not type(height) is int:
            raise TypeError('width must be an integer')
        if height < 0 or width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = '#'

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height is 0 or self.width is 0:
            perimeter = 0
        else:
            perimeter = self.__height * 2 + self.__width * 2
        return (perimeter)

    def __str__(self):
        if self.__width is 0 or self.__height is 0:
            rectangle_str = ''
        else:
            rectangle_str = str(
                (str(self.print_symbol) * self.__width + '\n') * self.__height)
        return(rectangle_str)

    def __repr__(self):
        return('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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
