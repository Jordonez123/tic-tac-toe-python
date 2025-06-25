from player import PlayerImpl
from board import Board

class Game:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.game_winner = None
    
    def set_player_order(self, player1_order: int, player2_order: int):
        self.player1.player_id = player1_order
        self.player2.player_id = player2_order
    
    def play_game(self):
        # ask players for their names and assign playing order
        self.set_up_players()
        # main game loop
        while True:
            # ask player 1 for their move
            player1_move = input("Player 1, what is your move?: ")
            # add player1's move to the board
            # check for a winner
                # if yes, update self.game_winner and break the loop
            # ask player 2 for their move
            # check for a winner
                # if yes, update self.game_winner and break the loop

    def get_game_winner(self) -> PlayerImpl:
        return self.game_winner

    def _get_game_captions(self):
        pass


