from player_abc import Player
from board import Board

class Game:
    def __init__(self, player1: Player, player2: Player, board: Board):
        self.player1 = player1
        self.player = player2
        self.board = board
        self.game_winner = None
    
    def set_player_order(self):
        pass
    
    def play_game(self):
        pass

    def get_game_winner(self) -> Player:
        return self.game_winner

    def _get_game_captions(self):
        pass


