#!/usr/bin/python3
"""is a empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True


class Rectangle(BaseGeometry):
    """empty class"""
    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        a = self.__width
        b = self.__height
        return a * b

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """empty class"""
    def __init__(self, size):
        if self.integer_validator("size", size):
            self.__size = size

    def area(self):
        a = self.__size
        return a * a

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__size, self.__size))
