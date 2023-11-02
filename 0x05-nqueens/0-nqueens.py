#!/usr/bin/python3
"""
N queens puzzle is the challenge of
placing N non-attacking queens on an
N×N chessboard
"""

import sys


def validate_input():
    """validate user input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    else:
        n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def n_queens():
    """n_queens main function"""

    def solve_n_queens(row, column):
        """solve n queens"""
        place = [[]]
        for queen in range(row):
            place = move_queen(queen, column, place)
        return place

    def move_queen(queen, column, place):
        """move queen through each column"""
        safe_place = []
        for position in place:
            for i in range(column):
                if is_safe_to_place(queen, i, position):
                    safe_place.append(position + [i])
        return safe_place

    def is_safe_to_place(queen, i, position):
        """check if place is safe to place a queen"""
        if i in position:
            return False
        else:
            for column in range(queen):
                if abs(position[column] - i) == queen - column:
                    return False
            return True

    n = validate_input()
    solutions = solve_n_queens(n, n)
    for i in solutions:
        co_ordinates = []
        for row_x, row_y in enumerate(i):
            co_ordinates.append([row_x, row_y])
        print(co_ordinates)


if __name__ == '__main__':
    n_queens()
