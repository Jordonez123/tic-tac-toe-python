import unittest
from board import Board
from game import Game
from player import PlayerImpl

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
        self.assertEqual(self.game.get_player_move(), ("top", "left"))
    
    def test_set_up_players(self):
        self.game.set_up_players()

        self.assertEqual(self.game.player1.name, "Jordan")
        self.assertEqual(self.game.player1.player_id, 0)
        self.assertEqual(self.game.player1.player_icon, "X")

        self.assertEqual(self.game.player2.name, "Jennifer")
        self.assertEqual(self.game.player2.player_id, 1)
        self.assertEqual(self.game.player2.player_icon, "O")


if __name__ == "__main__":
    unittest.main()