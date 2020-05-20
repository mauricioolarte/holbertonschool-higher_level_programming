#!/usr/bin/python3
""" this is for init a class square"""


class Square():
    """this class is a square
    Args: None
    Attributes:
        size (int):is a integer.
    """
    def __init__(self, size=0):
        """ this for init fuction
        Args:
            size(int)
        """
        if (type(size) != str):
            if (size >= 0):
                self.__size = int(size)
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
