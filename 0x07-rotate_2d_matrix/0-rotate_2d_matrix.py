#!/usr/bin/python3
"""Rotate n x n 2D matrix to 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Initializing using tuple packing and unpacking
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
