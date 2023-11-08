#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx1, row in enumerate(new_matrix):
        for idx3, col in enumerate(new_matrix):
            new_matrix[idx1][idx3] = row[idx3] ** 2
    return new_matrix 
