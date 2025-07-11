from player import PlayerImpl
from board import Board

class Game:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self._game_winner = None

    def get_player_move(self) -> tuple[str, str]:
        player_move_row = input("Please enter the row position (top, middle, bottom): ")
        player_move_column = input("Please enter the column position (left, middle, right): ")
        return (player_move_row, player_move_column)

    def get_valid_player_move(self, player: PlayerImpl) -> tuple[str, str]:
        """
        Keeps requesting a move from the user until a valid move is provided.
        """
        while True:
            try:
                move = self.get_player_move()
                player.make_move(move, self.board)
                return move  # valid move executed, return
            except ValueError as e:
                print(f"Invalid move: {e}")
                print("Please try again.\n")

    def process_game_over(self):
        """
        Determine and set the game winner based on the current game state.
        """
        game_status = self.board.current_game_state()

        if game_status == "X wins":
            self._game_winner = self.player1 if self.player1.player_icon == "X" else self.player2
        elif game_status == "O wins":
            self._game_winner = self.player1 if self.player1.player_icon == "O" else self.player2
        else:
            self._game_winner = None

    def play_game(self) -> None:
        print("")
        print(self.board)

        while True:
            first_player = self.player1 if self.player1.player_id == 0 else self.player2
            second_player = self.player1 if self.player1.player_id == 1 else self.player2

            print(f"-------- {first_player.name} --------")
            self.get_valid_player_move(first_player)
            print("")
            if self.board.is_game_over():
                self.process_game_over()
                break

            print(self.board)
            print("")

            print(f"-------- {second_player.name} --------")
            self.get_valid_player_move(second_player)
            print("")
            if self.board.is_game_over():
                self.process_game_over()
                break

            print(self.board)
            print("")

        print(self.board)
        self._get_game_captions()
        print("")
        print("")

    def get_game_winner(self) -> PlayerImpl:
        return self._game_winner

    def _get_game_captions(self):
        print("|Summary of the game|")
        game_winner = self.get_game_winner()
        if game_winner:
            print(f"|---- {game_winner.name} won ----|")
        else:
            print(f"|---- The game came to a draw ----|")
