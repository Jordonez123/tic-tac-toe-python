class Board:
    def __init__(self):
        self.board = [["?" for _ in range(3)] for _ in range(3)]

    def __len__(self):
        """
        Allow for direct len call on the Board Object.
        """
        return len(self.board)
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
        if mark not in "XO":
            raise ValueError("Cannot use an invalid mark on the board.")
        self.board[row][col] = mark
    
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
        self.board = [["?" for _ in range(3)] for _ in range(3)]

    def get_empty_cells(self):
        """
        Returns a list of (row, col) tuples for available moves.
        """
        empty_cells = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[0])) if self.board[i][j] == "?"]

        return empty_cells

    def is_full(self):
        """
        Returns True if all cells are filled.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[1])):
                if self.board[i][j] == "?":
                    return False
        
        return True

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
        Returns True for a positive case. Returns False otherwise.
        """
        
        # out of bounds check
        if not 0 <= row < len(self.board) and not 0 <= col < len(self.board[0]):
            return False
        # empty cell check
        if self.board[row][col] != "?":
            return False
        
        # all checks passed
        return True

    # -------------------------- Winner Checks ------------------------------------
    def _check_winner(self, mark: str):
        """
        Private function to actually do the work.
        Check for each row, column, left diagonal, and right diagonal.

        mark: the player that we are currently checking for. Either "X" or "O".
        """

        # used to check
        comparator = [mark] * 3

        print(comparator)
        # check each row
        for row in self.board:
            if row == comparator:
                return True
        
        # check each column

        for column in range(len(self.board)):
            column_values = [self.board[row][column] for row in range(len(self.board))]
            if column_values == comparator:
                return True
        
        # check left diagonal
        left_diagonal = [self.board[row][row] for row in range(len(self.board))]
        if left_diagonal == comparator:
            return True

        # check right diagonal
        right_diagonal = [self.board[row][len(self.board) - 1 - row] for row in range(len(self.board))]
        if right_diagonal == comparator:
            return True
        
        # no winner has been found for the mark parameter
        return None
    def check_winner(self):
        """
        Check if there a winner (return "X", "O", or None).
        """
        
        # check if X won
        if self._check_winner("X"):
            return "X"
        # check if O won
        elif self._check_winner("O"):
            return "O"
        # if none of the above is true then either draw
        # or game is still in progress.
        # regardless, return None
        return None

    # -------------------------- Game State ------------------------------------
    def current_game_state(self):
        """
        Returns a status like "X wins", "O wins", "Draw", or "In Progress".
        """
        pass

    def is_game_over(self):
        """
        True if either someone won or the board is full.
        """
        pass

    