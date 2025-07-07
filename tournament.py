from game import Game
from player_abc import Player
from collections import defaultdict

class Tournament:
    def __init__(self):
        self.number_of_games = None
        self.tournament_ended = False
        self.tournament_winner = None
        self.player_scores = defaultdict(int)

    def set_up_players(self) -> None:
        # Ask player 1 for name and assign playing order
        player1_name = input("Player 1 Name: ")
        self.player1.set_player_id(0)
        self.player1.name = player1_name
        # Ask player 2 for name and assign playing order
        player2_name = input("Player 2 Name: ")
        self.player2.set_player_id(1)
        self.player2.name = player2_name
        # Assign icons "X" or "O" for player 1 and player respectively
        self.player1.set_player_icon("X")
        self.player2.set_player_icon("O")

    def create_new_game(self, player1: Player, player2: Player):
        pass
    
    def start_tournament(self):
        pass

    def get_tournament_winner(self) -> Player:
        return self.tournament_winner
    
    def display_tournament_winner(self) -> str:
        pass
