#!/usr/bin/python3
""" this module do the add of two integer



"""


def add_integer(a, b=98):
    """ this function add two integer
    Arguments: a, b: int
    Return: integer """
    argu = [a, b]
    sum = 0
    if type(a) == list:
        raise TypeError('a must be an integer')
    if a is None or type(a) == str:
        raise TypeError('a must be an integer')
        return
    if type(a) != int and type(a) != float:
        raise NameError('a must be an integer')
    if type(b) == str or type(b) == list:
        raise TypeError('b must be an integer')
    if type(b) != int and type(b) != float:
            raise NameError('b must be an integer')
    for element in argu:
        if (type(element) == int or type(element) == float):
            sum += int(element)
    return sum

if __name__ == '__main__':
    import doctest
    doctest.testfile(0-add_integer)
