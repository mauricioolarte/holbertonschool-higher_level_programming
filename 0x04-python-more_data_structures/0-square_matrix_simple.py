#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[column[i] for column in matrix] for i in range(len(matrix))]
    new_matrix2 = [[row[i] for row in matrix] for i in range(len(matrix))]
    # for i in range(len(matrix)):
    #     print(len(matrix[i]))

    # new_matrix = []
    # print(len(matrix))
    # for i in range(len(matrix)):
    #     new_matrix[i] = []
    #     for j in range(len(matrix[i])):
    #         new_matrix[j].append(matrix[i][j] ** 2)
    return (new_matrix)