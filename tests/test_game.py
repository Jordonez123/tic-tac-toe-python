import unittest
from board import Board
from game import Game
from player import PlayerImpl
from unittest.mock import MagicMock, patch

class TestGame(unittest.TestCase):
    # -------------------------- Set Up and Tear Down ------------------------------------
    def setUp(self):
        self.player1 = PlayerImpl("")
        self.player2 = PlayerImpl("")
        self.board = Board()
        self.game = Game(self.player1, self.player2, self.board)

    def tearDown(self):
        self.player1 = None
        self.player2 = None
        self.board = None
        self.game = None

# -------------------------- Player functionality ------------------------------------
    def test_get_player_move(self):
        print("--------test_get_player_move--------")
        self.assertEqual(self.game.get_player_move(), ("top", "left"))
    
    @patch("builtins.input")
    @patch("builtins.print")  # suppress prints
    def test_play_game_x_wins_top_row(self, mock_print, mock_input):
        print("--------test_play_game_x_wins_top_row(game mocked)--------")
        # Mock inputs:
        # Player 1 name, Player 2 name
        # Player 1 move: "top", "left"
        # Player 2 move: "middle", "left"
        # Player 1 move: "top", "middle"
        # Player 2 move: "middle", "middle"
        # Player 1 move: "top", "right" (winning move)
        mock_input.side_effect = [
            "Alice", "Bob",          # player names
            "top", "left",           # player 1
            "middle", "left",        # player 2
            "top", "middle",         # player 1
            "middle", "middle",      # player 2
            "top", "right"           # player 1 (wins)
        ]

        # Act
        self.game.play_game()

        # Assert
        self.assertEqual(self.game.game_winner, "X")
        # Board should reflect:
        # X | X | X
        # O | O | ?
        # ? | ? | ?

        expected_board = [
            ["X", "X", "X"],
            ["O", "O", "?"],
            ["?", "?", "?"]
        ]
        self.assertEqual(self.game.board.board, expected_board)
    
    def test_get_game_winner(self):
        print("----test_get_game_winner(playing an actual game)--------")
        self.game.play_game()
        self.assertEqual(self.game.get_game_winner(), "X")

if __name__ == "__main__":
    unittest.main()