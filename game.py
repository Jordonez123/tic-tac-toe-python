from player import PlayerImpl
from board import Board

class Game:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self._game_winner = None
    
    def get_player_move(self) -> tuple[str, str]:
        print("Enter one of the following positions for the row move: [top, middle, bottom].")
        player_move_row = input("Please enter the row position: ")
        print("Enter one of the following positions for the column move: [left, middle, right].")
        player_move_column = input("Please enter the column position: ")
        return (player_move_row, player_move_column)
    
    def process_game_over(self):
        """
        Determine and set the game winner based on the current game state.
        """
        # Check if the game is over
        # If yes, then get the status code of the game
        # There is a clear winner or a draw
        game_status = self.board.current_game_state()

        if game_status == "X wins":
            self._game_winner = self.player1 if self.player1.player_icon == "X" else self.player2
        elif game_status == "O wins":
            self._game_winner = self.player1 if self.player1.player_icon == "O" else self.player2
        else:
            self._game_winner = None

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

    def get_game_winner(self) -> PlayerImpl:
        return self._game_winner

    def _get_game_captions(self):
        print("|Summary of the game|")
        game_winner = self.get_game_winner()
        if game_winner:
            print(f"|---- {game_winner.name} won ----|")
        else:
            print(f"|---- The game came to a draw ----|")
            
