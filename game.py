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

    def set_up_players(self):
        # Ask player 1 for name and assign playing order
        player1_name = input("Player 1 Name: ")
        self.player1.set_player_id(0)
        self.player1.name = player1_name
        # Ask player 2 for name and assign playing order
        player2_name = input("Player 2 Name: ")
        self.player2.set_player_id(1)
        self.player2.name = player2_name
    
    def get_player_move(self) -> tuple[str, str]:
        print("Enter one of the following positions for the row move: [top, middle, bottom].")
        player_move_row = input("Please enter the row position: ")
        print("Enter one of the following positions for the column move: [left, middle, right].")
        player_move_column = input("Please enter the column position: ")
        return player_move_row, player_move_column
    
    def play_game(self):
        # Ask players for their names and assign playing order
        self.set_up_players()
        # main game loop
        while True:
            # Ask player 1 for their move
            player1_move_row, player1_move_column = self.get_player_move()
            # Add player 1 move to the board
            self.player1.make_move(player1_move_row, player1_move_column, self.board)
            # Check for a winner
            winner_check = self.board.check_winner()
            # If yes, update self.game_winner and break the loop
            if winner_check:
                    self.game_winner = winner_check
                    break
            # Ask player 2 for their move
            player2_move_row, player2_move_column = self.get_player_move()
            # Add player 2 move to the board
            self.player2.make_move(player2_move_row, player2_move_column, self.board)
            # Check for a winner
            winner_check = self.board.check_winner()
            # If yes, update self.game_winner and break the loop
            if winner_check:
                 self.game_winner = winner_check
                 break

    def get_game_winner(self) -> PlayerImpl:
        return self.game_winner

    def _get_game_captions(self):
        pass


