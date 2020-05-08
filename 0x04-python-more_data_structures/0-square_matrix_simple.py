#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        file = []
        for j in range(len(matrix[i])):
            file.append(matrix[i][j] ** 2)
        new_matrix.append(file)
    return (new_matrix)
