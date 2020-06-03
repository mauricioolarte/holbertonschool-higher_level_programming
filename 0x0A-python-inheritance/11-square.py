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


class Square(BaseGeometry):
    """empty class"""
    def __init__(self, width):
        if self.integer_validator("width", width):
            self.__width = width

    def area(self):
        a = self.__width
        return a * a

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__width, self.__width))
