class Board:
    def __init__(self):
        self.board = [["?" for _ in range(3)] for _ in range(3)]
        self.current_turn = None
        
    def display_board(self):
        pass

    def get_next_move(self):
        pass

    def check_if_valid_move(self, move: tuple) -> bool:
        """Logic for checking if the current move is a valid move.
        
        1. Assure that the proposed move location is empty.
        2. Function should not be able to be called if there's no order.
        3. Assure that the move is not empty (we actually captured a move from the player).
        assignment."""

        if not move:
            raise Exception
        pass
