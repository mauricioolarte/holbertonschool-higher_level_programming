#!/usr/bin/python3
"""doc"""


from models.base import Base


class Rectangle(Base):
    """doc"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError('width must be and integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be and integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError('x must be and integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError('y must be and integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be and integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be and integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be and integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be and integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
