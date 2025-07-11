#!/usr/bin/python3
"""
N Queens puzzle solver using backtracking algorithm.
Usage: nqueens N
"""

import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe.

    Args:
        board: Current board state
        row: Row to place queen
        col: Column to place queen

    Returns:
        bool: True if safe, False otherwise
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on left side
    for i in range(row):
        if board[i] == col - (row - i):
            return False

    # Check upper diagonal on right side
    for i in range(row):
        if board[i] == col + (row - i):
            return False

    return True


def solve_nqueens(n, board, row, solutions):
    """
    Solve N Queens using backtracking.

    Args:
        n: Size of the chessboard
        board: Current board state (list of column positions)
        row: Current row being processed
        solutions: List to store all solutions
    """
    # Base case: if all queens are placed
    if row == n:
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        solutions.append(solution)
        return

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1, solutions)


def main():
    """Main function to handle command line arguments and solve N Queens."""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board and solutions
    board = [-1] * n
    solutions = []

    # Solve N Queens
    solve_nqueens(n, board, 0, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
