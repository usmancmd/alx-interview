#!/usr/bin/python3
"""Pascal's triangle challenge"""


def pascal_triangle(n):
    """Return list of lists of integers that represent pascal triangle"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

        return triangle
