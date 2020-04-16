import unittest

ttt = __import__('tictactoe')


class TicTacToeTests(unittest.TestCase):

    def test_terminal_empty_board_returns_false(self):
        board = ttt.initial_state()
        result = ttt.terminal(board)
        self.assertEqual(False, result)

    def test_X_in_horizontal_lines_returns_true(self):
        board1 = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None]
        ]
        board2 = [
            [None, None, None],
            ['X', 'X', 'X'],
            [None, None, None]
        ]
        board3 = [
            [None, None, None],
            [None, None, None],
            ['X', 'X', 'X']
        ]
        result1 = ttt.terminal(board1)
        result2 = ttt.terminal(board2)
        result3 = ttt.terminal(board3)
        self.assertEqual(True, result1)
        self.assertEqual(True, result2)
        self.assertEqual(True, result3)

    def test_X_in_vertical_lines_returns_true(self):
        board1 = [
            ['X', None, None],
            ['X', None, None],
            ['X', None, None]
        ]
        board2 = [
            [None, 'X', None],
            [None, 'X', None],
            [None, 'X', None]
        ]
        board3 = [
            [None, None, 'X'],
            [None, None, 'X'],
            [None, None, 'X']
        ]
        result1 = ttt.terminal(board1)
        result2 = ttt.terminal(board2)
        result3 = ttt.terminal(board3)
        self.assertEqual(True, result1)
        self.assertEqual(True, result2)
        self.assertEqual(True, result3)

    def test_X_in_diagonal_returns_true(self):
        board = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X']
        ]
        result = ttt.terminal(board)
        self.assertEqual(result, True)

    def test_create_diagonal_matrix_left(self):
        matrix = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X']
        ]
        diagonal_matrix = ttt.create_diagonal_matrix(matrix)
        self.assertEqual(diagonal_matrix, [
            ['X', None, None],
            ['X', None, None],
            ['X', None, None]
        ])

    def test_create_diagonal_matrix_right(self):
        matrix = [
            [None, None, 'X'],
            [None, 'X', None],
            ['X', None, None]
        ]
        diagonal_matrix = ttt.create_diagonal_matrix(matrix, 'right')
        self.assertEqual(diagonal_matrix, [
            [None, None, 'X'],
            [None, None, 'X'],
            [None, None, 'X']
        ])

    def test_board_is_draw_returns_true(self):
        board = [
            ['O', 'X', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'X']
        ]
        result = ttt.terminal(board)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
