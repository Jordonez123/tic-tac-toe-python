import unittest
from unittest.mock import MagicMock, patch
from tournament import Tournament
from player import PlayerImpl
from game import Game
from board import Board

class TestTournament(unittest.TestCase):
    def setUp(self):
        self.player1 = PlayerImpl("Player1")
        self.player2 = PlayerImpl("Player2")
        self.tournament = Tournament(self.player1, self.player2)

    def tearDown(self):
        self.player1 = None
        self.player2 = None
        self.tournament = None

    @patch("builtins.input", side_effect=["Jordan", "Jennifer"])
    def test_set_up_players(self, mock_input):
        self.tournament.set_up_players()
        self.assertEqual(self.tournament.player1.name, "Jordan")
        self.assertEqual(self.tournament.player2.name, "Jennifer")

    @patch("time.sleep", return_value=None)
    @patch("random.randint", side_effect=[0, 1, 0])
    def test_play_single_game_records_winner(self, mock_randint, mock_sleep):
        # Mock _create_new_game to return a mock game with get_game_winner
        mock_game = MagicMock()
        mock_game.get_game_winner.return_value = self.player1
        self.tournament._create_new_game = MagicMock(return_value=mock_game)

        # Execute _play_single_game
        self.tournament._play_single_game(1)

        # Assert winner recorded
        scores = self.tournament.get_player_scores()
        self.assertEqual(scores[self.player1.name], 1)

    @patch("builtins.input", side_effect=["Jordan", "Jennifer"])
    @patch("time.sleep", return_value=None)
    @patch("random.randint", side_effect=[0, 1, 0])  # force playing order
    def test_start_tournament_updates_scores_and_winner(self, mock_randint, mock_sleep, mock_input):
        # Mock _create_new_game to return a mock game
        mock_game = MagicMock()
        self.tournament._create_new_game = MagicMock(return_value=mock_game)

        # Simulate get_game_winner returns: player1, player1, None (draw)
        mock_game.get_game_winner.side_effect = [self.player1, self.player1, None]

        # Act
        self.tournament.start_tournament()

        # Assert
        self.assertTrue(self.tournament.tournament_ended)
        scores = self.tournament.get_player_scores()
        self.assertEqual(scores[self.player1.name], 2)
        self.assertEqual(scores[self.player2.name], 0)
        self.assertEqual(self.tournament.get_tournament_winner(), self.player1.name)
        self.assertEqual(mock_game.play_game.call_count, 3)
        self.assertEqual(mock_game.get_game_winner.call_count, 3)

if __name__ == "__main__":
    unittest.main()
