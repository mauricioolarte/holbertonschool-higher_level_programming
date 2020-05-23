#!/usr/bin/python3
"""function that divides all elements of a matrix.
    arg: matrix: is a list of list of integer/floats, div: is int/float
    Return: matrix
    """


def matrix_divided(matrix, div):
    """ this take a matrix and divid for div
    arg: matrix: is a list of list of integer/floats, div: is int/float
    Return: matrix
    """
    # matrix must be a list of lists of integers or floats
    if matrix is [] or matrix is '':
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if matrix is None:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    # matrix must be a list of lists of integers or floats
    for i in matrix:
        if not type(i) is list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for j in i:
            if not type(j) in [int, float]:
               raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')

    # Each row of the matrix must be of the same size
    comparador = len(matrix[0]) # matrix[0] por ser inicio de arreglo
    for i in matrix:
        if len(i) != comparador:
            raise TypeError('Each row of the matrix must have the same size')
        else:
            comparador = len(i)

    # div must be a number (integer or float)
    if not type(div) in [float, int]:
        raise TypeError('div must be a number')

    # div must be != 0
    if div is 0:
        raise ZeroDivisionError('division by zero')

    # fucntion matrix divided
    new_matrix = [0] * len(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = [0] * len(matrix[i])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return(new_matrix)
if __name__ == '__main__':
    import doctest
    doctest.testfile(2-matrix_divided)
