#!/usr/bin/python3
"""
Calculate the perimeter of a island in grid
"""


def island_perimeter(grid):
    """Returns island perimeter"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check the four adjacent cells
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # for the top edge
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # for the bottom edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # for the left edge
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # for the right edge

    return perimeter
