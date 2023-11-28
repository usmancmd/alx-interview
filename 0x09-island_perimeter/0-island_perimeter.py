#!/usr/bin/python3
"""
Calculate the perimeter of a island in grid
"""


def island_perimeter(grid):
    """Returns island perimeter"""
    perimeter = 0
    for i, v in enumerate(grid):
        for j, k in enumerate(v):
            if k == 1:
                if j == 0:
                    perimeter += 1
                    if v[j + 1] == 0:
                        perimeter += 1
                elif j == len(grid[0]):
                    if v[j - 1] == 0:
                        perimeter += 1
                    perimeter += 1
                else:
                    if v[j - 1] == 0:
                        perimeter += 1
                    if v[j + 1] == 0:
                        perimeter += 1

                if i == 0:
                    perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                elif i == len(grid):
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    perimeter += 1
                else:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
    return perimeter
