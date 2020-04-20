"""
Tic Tac Toe Player
"""

import math
from copy import copy, deepcopy

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
    if terminal(board):
        return None

    if board == initial_state():
        return X

    x_count = 0
    o_count = 0
    for row in board:
        for place in row:
            if place == X:
                x_count += 1
            elif place == O:
                o_count += 1

    if x_count > o_count:
        return O
    elif x_count < o_count:
        return X
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    result = []
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == None:
                result.append((i, j))
    return set(result)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_result = utility(board)
    if win_result == 1:
        return X
    elif win_result == -1:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win_result = utility(board)
    if win_result == 1 or win_result == -1:
        return True

    # Check for all places filled:
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
        row_win_result = check_row_for_win(row)
        if row_win_result[0]:
            return row_win_result
    return (False, None)


def check_row_for_win(row):
    return (len(set(row)) == 1 and row[0] != EMPTY, row[0])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = None
    horizontal_win_result = check_board_for_win(board)
    vertical_win_result = check_board_for_win(zip(*board))
    left_diagonal_as_row = list(zip(*create_diagonal_matrix(board, "left")))[0]
    right_diagonal_as_row = list(
        zip(*create_diagonal_matrix(board, "right")))[-1]

    left_diagonal_win_result = check_row_for_win(left_diagonal_as_row)
    right_diagonal_win_result = check_row_for_win(right_diagonal_as_row)

    if horizontal_win_result[0]:
        winner = horizontal_win_result[1]
    elif vertical_win_result[0]:
        winner = vertical_win_result[1]
    elif left_diagonal_win_result[0]:
        winner = left_diagonal_win_result[1]
    elif right_diagonal_win_result[0]:
        winner = right_diagonal_win_result[1]

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    return minimax_impl(board, None)[0]


def minimax_impl(board, action):
    if terminal(board):
        return (action, utility(board))

    current_player = player(board)
    next_actions = actions(board)
    minimax = (None, -2 if player == X else 2)
    for act in next_actions:
        _, value = minimax_impl(result(board, act), act)
        if player == 'X':
            if value > minimax[1]:
                minimax = (act, value)
        else:
            if value < minimax[1]:
                minimax = (act, value)
    return minimax
