#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Division function for a matrix"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("Each row of the matrix must have the same size")

    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row] for row in matrix]
    return new_matrix
