#!/usr/bin/python3
"""A program that solves the N queens puzzle"""

import sys


def set_board(length):
    """Sets a chessboard of size len x len and initializes with zeroes"""
    board = []
    [board.append([]) for i in range(length)]
    [row.append(' ') for i in range(length) for row in board]
    return (board)

def duplicate(board):
    """Returns a deepcopy of a chessboard"""
    if isinstance(board, list):
        return list(map(duplicate, board))
    return (board)

def get_result(board):
    """Returns a solved chessboard as an array of lists"""
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                result.append([i, j])
                break
    return (result)

# def mark_x(board, row, column):
    """It is marks out tiles on a board
        Where a queen is prohibited to roam, the tiles are marked.

        Args:
            board(list): The chessboard(present)
            row(int): Queen's last row position
            column(int): Queen's last column position
    """
    size = len(board)
    for col in range(column + 1, size):
        board[row][col] = "x"
    for col in range(column - 1, -1, -1):
        board[row][col] = "x"
    for r in range(row + 1, size):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    
    col = column + 1
    for r in range(row + 1, size):
        if col >= size:
            break
        board[r][col] = "x"
        col += 1
    col = column - 1
    for r in range(row - 1, -1, -1):
        if col < 0:
            break
        board[r][col] = "x"
        col -= 1

    col = column + 1
    for r in range(row - 1, -1, -1):
        if col >= size:
            break
        board[r][col] = "x"
        col += 1

    for r in range(row - 1, -1, -1):
        if col < 0:
            break
        board[r][col] = "x"
        col -= 1

def mark_x(board, row, column):
    """Marks out tiles on a board where a queen is prohibited to roam."""
    size = len(board)
    # Mark horizontally and vertically
    for i in range(size):
        board[row][i] = "x"
        board[i][column] = "x"

    # Mark diagonally
    for i, j in zip(range(row + 1, size), range(column + 1, size)):
        if i >= size or j >= size:
            break
        board[i][j] = "x"

    for i, j in zip(range(row - 1, -1, -1), range(column + 1, size)):
        if i < 0 or j >= size:
            break
        board[i][j] = "x"

    for i, j in zip(range(row + 1, size), range(column - 1, -1, -1)):
        if i >= size or j < 0:
            break
        board[i][j] = "x"

    for i, j in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
        if i < 0 or j < 0:
            break
        board[i][j] = "x"

def repeat(board, row, queen, result):
    if queen == len(board):
        result.append(get_result(board))
        return(result)

    for col in range(len(board)):
        if board[row][col] == " ":
            temp = duplicate(board)
            temp[row][col] = "Q"
            mark_x(temp, row, col)
            result = repeat(temp, row + 1, queen + 1, result)
    return(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    board = set_board(int(sys.argv[1]))
    result = repeat(board, 0, 0, [])
    for each in result:
        print(each)