import unittest
from unittest.mock import patch
from board import Board
from game import Game
from player import PlayerImpl

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = PlayerImpl("Jordan")
        self.player2 = PlayerImpl("Jennifer")

        self.player1.set_player_id(0)
        self.player1.set_player_icon("X")

        self.player2.set_player_id(1)
        self.player2.set_player_icon("O")

        self.board = Board()
        self.game = Game(self.player1, self.player2, self.board)

    def tearDown(self):
        self.player1 = None
        self.player2 = None
        self.board = None
        self.game = None

    @patch("builtins.input", side_effect=["top", "left"])
    def test_get_player_move(self, mock_input):
        move = self.game.get_player_move()
        self.assertEqual(move, ("top", "left"))

    @patch("builtins.input")
    @patch("builtins.print")  # suppress prints during test
    def test_play_game_x_wins_top_row(self, mock_print, mock_input):
        # Arrange: Moves to ensure player1 (X) wins top row
        # Player 1: top-left, top-middle, top-right
        # Player 2: middle-left, middle-middle
        mock_input.side_effect = [
            "top", "left",        # P1
            "middle", "left",     # P2
            "top", "middle",      # P1
            "middle", "middle",   # P2
            "top", "right"        # P1 wins
        ]

        # Act
        self.game.play_game()

        # Assert winner is player1
        self.assertIsNotNone(self.game.get_game_winner())
        self.assertEqual(self.game.get_game_winner().name, "Jordan")

        # Assert board state
        expected_board = [
            ["X", "X", "X"],
            ["O", "O", "?"],
            ["?", "?", "?"]
        ]
        self.assertEqual(self.board.board, expected_board)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_play_game_o_wins_column(self, mock_print, mock_input):
        # Arrange: Moves to ensure player2 (O) wins left column
        # Player 1: top-middle, middle-middle, bottom-middle
        # Player 2: top-left, middle-left, bottom-left
        mock_input.side_effect = [
            "top", "middle",      # P1
            "top", "left",        # P2
            "middle", "middle",   # P1
            "middle", "left",     # P2
            "bottom", "middle",   # P1
            "bottom", "left"      # P2 wins
        ]

        # Act
        self.game.play_game()

        # Assert winner is player2
        self.assertIsNotNone(self.game.get_game_winner())
        self.assertEqual(self.game.get_game_winner().name, "Jennifer")

        # Assert board state
        expected_board = [
            ["O", "X", "?"],
            ["O", "X", "?"],
            ["O", "X", "?"]
        ]
        self.assertEqual(self.board.board, expected_board)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_game_draw(self, mock_print, mock_input):
        # Arrange: Force a draw
        # Board state after:
        # X | O | X
        # X | O | O
        # O | X | X
        mock_input.side_effect = [
            "top", "left",        # P1
            "top", "middle",      # P2
            "top", "right",       # P1
            "middle", "right",    # P2
            "middle", "left",     # P1
            "middle", "middle",   # P2
            "bottom", "middle",   # P1
            "bottom", "left",     # P2
            "bottom", "right"     # P1
        ]

        # Act
        self.game.play_game()

        # Assert the game is a draw
        self.assertIsNone(self.game.get_game_winner())

        expected_board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertEqual(self.board.board, expected_board)

if __name__ == "__main__":
    unittest.main()
