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
        if (type(size) == int):
            if (size >= 0):
                self.__size = int(size)
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ this is the area of a square
        Args:
            None.
        Return:
            area(int): is an area of square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ this is for retrive a private value of size
        Args:
            None.
        Return:
            size(int): is a size of square.
        """
        return (self.__size)

    @size.setter
    def size(self, value=0):
        """ this is for retrive a private value of size
        Args:
            None.
        Return:
            size(int): is a size of square.
        """
        if (type(value) == int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """ this print the square whit # symbol
        Args:
            none
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                if j == self.size - 1:
                    print('#')
                else:
                    print('#'.format(), end='')
