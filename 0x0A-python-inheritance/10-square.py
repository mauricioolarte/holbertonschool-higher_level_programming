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

class Square(Rectangle):
    """empty class"""
    def __init__(self, width):
        if self.integer_validator("width", width):
            self.__width = width

    def area(self):
        a = self.__width
        return a * a

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__width))
