import unittest

ttt = __import__('tictactoe')

horizonal_wins = [
    [
        ['X', 'X', 'X'],
        [None, None, None],
        [None, None, None]
    ],
    [
        [None, None, None],
        ['X', 'X', 'X'],
        [None, None, None]
    ],
    [
        [None, None, None],
        [None, None, None],
        ['X', 'X', 'X']
    ]
]

vertical_wins = [
    [
        ['X', None, None],
        ['X', None, None],
        ['X', None, None]
    ],
    [
        [None, 'X', None],
        [None, 'X', None],
        [None, 'X', None]
    ],
    [
        [None, None, 'X'],
        [None, None, 'X'],
        [None, None, 'X']
    ]
]

draw_board = [['O', 'X', 'O'],
              ['O', 'X', 'X'],
              ['X', 'O', 'X']]


class TicTacToeTests(unittest.TestCase):

    def test_terminal_empty_board_returns_false(self):
        board = ttt.initial_state()
        result = ttt.terminal(board)
        self.assertEqual(False, result)

    def test_X_in_horizontal_lines_returns_true(self):
        for board in horizonal_wins:
            result = ttt.terminal(board)
            self.assertEqual(True, result)

    def test_X_in_vertical_lines_returns_true(self):
        for board in vertical_wins:
            result = ttt.terminal(board)
            self.assertEqual(True, result)

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
        result = ttt.terminal(draw_board)
        self.assertEqual(result, True)

    def test_player_initial_state_returns_X(self):
        self.assertEqual('X', ttt.player(ttt.initial_state()))

    def test_player_same_amout_of_X_and_O_returns_X(self):
        board = [
            ['X', None, None],
            ['O', None, None],
            [None, None, None]
        ]
        self.assertEqual('X', ttt.player(board))

    def test_more_X_than_O_returns_O(self):
        board = [
            ['X', None, None],
            ['O', None, None],
            [None, 'X', None]
        ]
        self.assertEqual('O', ttt.player(board))

    def test_more_O_than_X(self):
        board = [
            ['X', None, None],
            ['O', None, None],
            [None, 'O', None]
        ]
        self.assertEqual('X', ttt.player(board))

    def test_player_gets_terminal_state_returns_none(self):
        self.assertIsNone(ttt.player(draw_board))

    def test_actions_terminal_board_retruns_none(self):
        self.assertIsNone(ttt.actions(draw_board))

    def test_actions_initial_state_returns_9_actions(self):
        expected_result = set([(x, y) for x in range(0, 3)
                               for y in range(0, 3)])
        self.assertEqual(expected_result, ttt.actions(ttt.initial_state()))

    def test_actions_two_places_returns_indexes(self):
        board = [
            ['X', None, 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', None]
        ]
        self.assertEqual(set([(0, 1), (2, 2)]), ttt.actions(board))

    def test_result_X_places_a_move_returns_correct_board(self):
        board = [
            ['X', None, None],
            ['O', None, None],
            [None, None, None]
        ]
        expected_result = [
            ['X', 'X', None],
            ['O', None, None],
            [None, None, None]
        ]
        action = (0, 1)
        self.assertEqual(expected_result, ttt.result(board, action))

    def test_result_O_places_a_move_returns_correct_board(self):
        board = [
            ['X', 'X', None],
            ['O', None, None],
            [None, None, None]
        ]
        expected_result = [
            ['X', 'X', None],
            ['O', None, None],
            ['O', None, None]
        ]
        action = (2, 0)
        self.assertEqual(expected_result, ttt.result(board, action))
        self.assertEqual([
            ['X', 'X', None],
            ['O', None, None],
            [None, None, None]
        ], board)

    def test_minimax_initial_state_X_can_move(self):
        result = ttt.minimax(ttt.initial_state())
        self.assertEqual((0, 1), result)


if __name__ == '__main__':
    unittest.main()
