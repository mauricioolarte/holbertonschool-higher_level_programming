#!/usr/bin/python3
""" this is for init a class square"""


class Square():
    """this class is a square
    Args: None
    Attributes:
        size (int):is a integer.
    """
    # def __init__(self, size=0):
    #     """ this for init fuction
    #     Args:
    #         size(int)
    #         position(int)
    #     """
    #     if (type(size) == int):
    #         if (size >= 0):
    #             self.__size = int(size)
    #         else:
    #             raise ValueError('size must be >= 0')
    #     else:
    #         raise TypeError('size must be an integer')

    # @property
    def __init__(self, size=0, position=(0, 0)):
        """ this for init fuction
        Args:
            size(int)
            position(int)
        """
        if (type(size) == int):
            if (size >= 0):
                self.__size = int(size)
            else:
                    raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

        if position:
            if (len(position) == 2 and type(position) == tuple and
                    type(position[1]) == int and type(position[0]) == int):
                if (int(position[1]) >= 0 and int(position[0]) >= 0):
                    self.__position = position
                else:
                    raise TypeError(
                        'position must be a tuple of 2 positive integers')
            else:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
        else:
            self.__position = (0, 0)

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
            value: tuple of postive integers.
        """
        if (type(value) == int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """ this is for retrive a private value of size
        Args:
            None.
        Return:
            position(int): is a coordenades of square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value[0]) == int and value[1] == int):
            if (value[1] >= 0 and value[0] >= 0):
                self.__position = value
            else:
                raise TypeError('position must be a tuple\
                    of 2 positive integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """ this print the square whit # symbol
            Args:
                none
        """
        if self.size == 0:
                print()
        else:
            for coordenadesx in range(self.position[1]):
                print()
            for i in range(self.size):
                print('{}'.format(" " * self.position[0]), end='')
                for j in range(self.size):
                    if j == self.size - 1:
                        print('#')
                    else:
                        print('#'.format(), end='')
