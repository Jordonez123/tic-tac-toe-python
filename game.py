from player import PlayerImpl
from board import Board

class Game:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.game_winner = None
    
    def get_player_move(self) -> tuple[str, str]:
        print("Enter one of the following positions for the row move: [top, middle, bottom].")
        player_move_row = input("Please enter the row position: ")
        print("Enter one of the following positions for the column move: [left, middle, right].")
        player_move_column = input("Please enter the column position: ")
        return (player_move_row, player_move_column)
    
    def process_game_over(self) -> None:
        # Check if the game is over
        # If yes, then get the status code of the game
        # There is a clear winner or a draw
        game_status_code = self.board.current_game_state()
        # Update self.game.winner
        if game_status_code == "X wins":
            self.game_winner = "X"
        elif game_status_code == "O wins":
            self.game_winner = "O"
        else:
            self.game_winner = "Draw"

    def play_game(self) -> None:
        # main game loop
        # Print the board
        print(self.board)
        while True:
            print("-------- Player 1 --------")
            # Ask player 1 for their move
            player1_move_row, player1_move_column = self.get_player_move()
            # Add player 1 move to the board
            self.player1.make_move((player1_move_row, player1_move_column), self.board)
            
            if self.board.is_game_over():
                self.process_game_over()
                # Stop the game
                break

            # Print the board
            print(self.board)

            print("---- Player 2 --------")
            # Ask player 2 for their move
            player2_move_row, player2_move_column = self.get_player_move()
            # Add player 2 move to the board
            self.player2.make_move((player2_move_row, player2_move_column), self.board)
            
            if self.board.is_game_over():
                self.process_game_over()
                # Stop the game
                break

            # Print the board
            print(self.board)

        # Print the board
        print(self.board)
        
        self._get_game_captions()

    def get_game_winner(self) -> str:
        return self.game_winner

    def _get_game_captions(self):
        print("|Summary of the game|")
        if self.game_winner:
            # Get the player with the winning icon
            if self.player1.player_icon == self.game_winner:
                print(f"|---- {self.player1.name} won ----|")
            else:
                print(f"|---- {self.player2.name} won ----|")
        else:
            print(f"|---- The game came to a draw ----|")
            
