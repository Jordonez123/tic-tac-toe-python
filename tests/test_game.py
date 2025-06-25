import unittest
from board import Board
from game import Game
from player import PlayerImpl

class TestGame(unittest.TestCase):
    # -------------------------- Set Up and Tear Down ------------------------------------
    def setUp(self):
        self.player1 = PlayerImpl("Jordan")
        self.player2 = PlayerImpl("Jennifer")
        self.board = Board()
        self.game = Game(self.player1, self.player2, self.board)

    def tearDown(self):
        self.player1 = None
        self.player2 = None
        self.board = None
        self.game = None

    def test_set_player_order(self):
        # player 1 goes first
        # player 2 goes second
        self.game.set_player_order(0, 1)
        self.assertEqual(self.player1.player_id, 0)
        self.assertEqual(self.player2.player_id, 1)

if __name__ == "__main__":
    unittest.main()