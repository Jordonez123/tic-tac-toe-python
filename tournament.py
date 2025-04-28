from game import Game
from player_abc import Player
from collections import defaultdict

class Tournament:
    def __init__(self, number_of_games: int):
        self.number_of_games = number_of_games
        self.tournament_ended = False
        self.tournament_winner = None
        self.player_scores = defaultdict(int)
    
    def get_tournament_winner(self) -> Player:
        return self.tournament_winner
    
    def display_tournament_winner(self) -> str:
        pass