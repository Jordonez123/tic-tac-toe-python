from player import PlayerImpl
from board import Board

class Game:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.game_winner = None

    def set_up_players(self):
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
    
    def get_player_move(self) -> tuple[str, str]:
        print("Enter one of the following positions for the row move: [top, middle, bottom].")
        player_move_row = input("Please enter the row position: ")
        print("Enter one of the following positions for the column move: [left, middle, right].")
        player_move_column = input("Please enter the column position: ")
        return (player_move_row, player_move_column)
    
    def play_game(self):
        # Ask players for their names and assign playing order
        self.set_up_players()
        # main game loop
        while True:
            # Ask player 1 for their move
            player1_move_row, player1_move_column = self.get_player_move()
            # Add player 1 move to the board
            self.player1.make_move((player1_move_row, player1_move_column), self.board)
            
            # Check if the game is over
            # If yes, then get the status code of the game
            # There is a clear winner or a draw
            # If not, then just continue the loop
            if self.board.is_game_over():
                game_status_code = self.board.current_game_state()
                # Update self.game.winner
                if game_status_code == "X wins":
                    self.game_winner = "X"
                elif game_status_code == "O wins":
                    self.game_winner = "O"
                else:
                    self.game_winner = "Draw"

                # Stop the game
                break
            
            # Ask player 2 for their move
            player2_move_row, player2_move_column = self.get_player_move()
            # Add player 2 move to the board
            self.player2.make_move((player2_move_row, player2_move_column), self.board)
            
            # Check if the game is over
            # If yes, then get the status code of the game
            # There is a clear winner or a draw
            # If not, then just continue the loop
            if self.board.is_game_over():
                game_status_code = self.board.current_game_state()
                # Update self.game.winner
                if game_status_code == "X wins":
                    self.game_winner = "X"
                elif game_status_code == "O wins":
                    self.game_winner = "O"
                else:
                    self.game_winner = "Draw"

                # Stop the game
                break
                    
    def get_game_winner(self) -> PlayerImpl:
        return self.game_winner

    def _get_game_captions(self):
        pass


