from game import Game
from player_abc import Player
from collections import defaultdict

class Tournament:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

        self.number_of_games = None
        self.tournament_ended = False
        self.tournament_winner = None
        self.player_scores = defaultdict(int)

    def create_new_game(self, player1: Player, player2: Player):
        pass
    
    def start_tournament(self):
        pass

    def get_tournament_winner(self) -> Player:
        return self.tournament_winner
    
    def display_tournament_winner(self) -> str:
        pass
