#!/usr/bin/python3
"""Solves the N Queens problem using backtracking"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        # Check vertical and diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Backtracking algorithm to solve the N Queens puzzle"""
    def backtrack(row, board):
        if row == n:
            # Format solution as [[row, col], ...]
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)

    solutions = []
    board = [-1] * n  # board[i] = column position of queen at row i
    backtrack(0, board)
    return solutions


def main():
    """Main program that handles input and prints solutions"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

