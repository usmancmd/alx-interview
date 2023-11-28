#!/usr/bin/python3
"""
Calculate the perimeter of a island in grid
"""


def island_perimeter(grid):
    """Returns island perimeter"""
    perimeter = 0
    count = 0
    for i, v in enumerate(grid):
        if sum(v) == 0:
            count += 1
        elif sum(v) == 1:
            count += 2
        elif sum(v) == 3:
            count += 6
    return count
