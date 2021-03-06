#!/usr/bin/python3
"""function that prints a square with the character #.

"""


def print_square(size):
    """function that prints a square with the character #
    arg: int or float
    return: noting
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and type(size) is float:
        raise TypeError('size must be an integer')
    if size is None:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            if j is size - 1:
                print('#')
            else:
                print('#', end='')
if __name__ == '__main__':
    import doctest
    doctest.testfile(4-print_square)
