#!/usr/bin/python3
"""module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
