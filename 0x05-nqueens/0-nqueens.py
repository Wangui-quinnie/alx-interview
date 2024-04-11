#!/usr/bin/python3
"""
Module: nqueens.py

This module solves the N Queens problem using backtracking algorithm.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the specified position on the board.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index of the position.
        col (int): The column index of the position.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    """
    Recursive function to solve the N Queens problem using backtracking.

    Args:
        board (list): The chessboard represented as a 2D list.
        col (int): The current column index being processed.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return False  # Continue searching for more solutions

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0

    return False


def nqueens(N):
    """
    Main function to solve the N Queens problem.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Raises:
        ValueError: If N is not an integer.

    Returns:
        None
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
