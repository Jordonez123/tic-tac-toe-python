class Board:
    def __init__(self):
        self.board = [["?" for _ in range(3)] for _ in range(3)]

    # -------------------------- Displays ------------------------------------

    def __str__(self):
        """
        Gives a string representation of the Board object.
        Useful for printing or debugging.
        """
        return '\n'.join(' | '.join(row) for row in self.board)
    
    # -------------------------- Update board ------------------------------------
    def place_mark(self, row: int, col: int, mark: str):
        """
        Place a mark ("X" or "O") on the board.
        """
        pass
    
    # -------------------------- Board Utilities ------------------------------------
   
    def __getitem__(self, index):
        """
        Allow board[row][col] indexing.
        """
        return self.board[index]
    
    def reset(self):
        """
        Reset the board to all "?" or empty marks.
        """
        pass

    def get_empty_cells(self):
        """
        Returns a list of (row, col) tuples for available moves.
        """
        pass

    def is_full(self):
        """
        Returns True if all cells are filled.
        """
        pass

    def copy(self):
        """
        Return a deep copy of the board.
        Useful for AI testing.
        """
        pass

    def undo_move(row: int, col: int):
        """
        Remove a mark.
        Good for bactracking in AI or testing.
        """
    
    # -------------------------- Valid Moves ------------------------------------
    def is_valid_move(self, row: int, col: int):
        """
        Check if a move is within bounds and on an empty cell.
        """
        pass

    # -------------------------- Winner Checks ------------------------------------
    def check_winner(self):
        """
        Check if there a winner (return "X", "O", or None).
        """
        pass

    # -------------------------- Game State ------------------------------------
    def current_game_state(self):
        """
        Returns a status like "X wins", "0 wins", "Draw", or "In Progress".
        """
        pass

    def is_game_over(self):
        """
        True if either someone won or the board is full.
        """
        pass

    