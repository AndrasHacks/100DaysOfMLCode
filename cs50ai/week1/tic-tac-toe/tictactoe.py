"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # horizontal check
    if check_board_for_win(board):
        return True

    # vertical check
    if check_board_for_win(zip(*board)):
        return True

    # left horizontal check:
    if check_row_for_win(list(zip(*create_diagonal_matrix(board, "left")))[0]):
        return True

    # right horizontal check:
    if check_row_for_win(list(zip(*create_diagonal_matrix(board, "right")))[-1]):
        return True

    if None not in set([item for sublist in board for item in sublist]):
        return True

    return False


def create_diagonal_matrix(matrix, side='left'):
    new_matrix = []
    for idx, row in enumerate(matrix):
        newRow = list(row)
        for shift in range(idx):
            if side == 'left':
                firstElement = newRow[0]
                del newRow[0]
                newRow.append(firstElement)
            else:
                lastElement = newRow[-1]
                del newRow[-1]
                newRow.insert(0, lastElement)
        new_matrix.append(newRow)
    return new_matrix


def check_board_for_win(board):
    for row in board:
        if check_row_for_win(row):
            return True
    return False


def check_row_for_win(row):
    return len(set(row)) == 1 and row[0] != EMPTY


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
