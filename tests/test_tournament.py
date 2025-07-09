import unittest
from tournament import Tournament
from player import PlayerImpl
from game import Game
from board import Board
from unittest.mock import MagicMock, patch

class TestGame(unittest.TestCase):
    # -------------------------- Set Up and Tear Down ------------------------------------
    def setUp(self):
        self.player1 = PlayerImpl("Player1")
        self.player2 = PlayerImpl("Player2")

        self.board = Board()
        self.game = Game(self.player1, self.player2, self.board)
        self.tournament = Tournament(self.player1, self.player2)

    def tearDown(self):
        self.player1 = None
        self.player2 = None
        self.board = None
        self.game = None

    def test_set_up_players(self):
        print("--------test_set_up_players--------")
        self.tournament.set_up_players()

        self.assertEqual(self.game.player1.name, "Jordan")
        self.assertEqual(self.game.player1.player_id, 0)
        self.assertEqual(self.game.player1.player_icon, "X")

        self.assertEqual(self.game.player2.name, "Jennifer")
        self.assertEqual(self.game.player2.player_id, 1)
        self.assertEqual(self.game.player2.player_icon, "O")
    
    def test_start_tournament_updates_scores_and_winner(self):
        # Arrange: create a mock Tournament object with required attributes
        tournament = Tournament(self.player1, self.player2)
        tournament.player_scores = {tournament.player1.name: 0, tournament.player2.name: 0}

        # Mock _create_new_game to return a mock game
        mock_game = MagicMock()
        tournament._create_new_game = MagicMock(return_value=mock_game)

        # Simulate get_game_winner returning player1 twice, None once
        mock_game.get_game_winner.side_effect = [tournament.player1, tournament.player1, None]

        # Act
        tournament.start_tournament()

        # Assert
        self.assertTrue(tournament.tournament_ended)
        self.assertEqual(tournament.player_scores[tournament.player1.name], 2)
        self.assertEqual(tournament.player_scores[tournament.player2.name], 0)
        self.assertEqual(tournament.tournament_winner, tournament.player1.name)
        self.assertEqual(mock_game.play_game.call_count, 3)
        self.assertEqual(mock_game.get_game_winner.call_count, 3)

if __name__ == "__main__":
    unittest.main()