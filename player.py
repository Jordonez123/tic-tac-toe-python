from player_abc import Player
from board import Board

class PlayerImpl(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def set_player_id(self, ID):
        if self.player_id is None:
            if ID is None:
                raise ValueError("Cannot assign an empty or NULL player ID.")
            elif ID not in (0, 1):
                raise ValueError("Player ID cannot be set to a non-binary value.")
            self.player_id = ID
        else:
            raise ValueError("Cannot overwrite previosuly assigned player ID.")
            
    def set_player_icon(self, icon: str):
        # Check that player ID is already set
        if self.player_id is not None:
            # Player icon has not been set already
            if self.player_icon is None:
                if icon is None:
                    raise ValueError("Player icon cannot be set to None or Empty.")
                elif icon not in "XO":
                    raise ValueError("Invalid Player icon assignment. Must assign a player icon of either X or O.")
                self.player_icon = icon
            # Player icon has been set, attempting invalid overriding
            else:
                raise ValueError(f"Player already has an icon: {self.player_icon}")
        else:
            raise ValueError("The player must have a valid player ID before attempting to assign a player icon.")


    def make_move(self, move: tuple[str, str], board: Board) -> None:
        """
        Function designed to check that the provided
        move is valid. Calls make_move() with the row and column
        positions if all checks are succesfully passed.

        Move will consist of a tuple of strings in 
        ["left", "middle", "right", "top", "bottom"]
        move = (x, y)
        Where x is either top, middle, or bottom row.
        This corresponds to row indices 0,1,2.
        where y is either left, middle, or right row.
        This corresponds to column indices of 0,1,2.
        """
        row_mapping = {"top": 0, "middle": 1, "bottom": 2}
        column_mapping = {"left": 0, "middle": 1, "right": 2}

        row_string, column_string = move

        # Check for None values for row or column
        if row_string is None or column_string is None:
            raise ValueError("Move must not have None values for either row or column directions.")
         # Check for inputs that are not string
        elif not isinstance(row_string, str) or not isinstance(column_string, str):
            raise ValueError("Move must be composed of valid string direction values.")
        # Check for non string values for row or column
        elif row_string.lstrip("-").isdigit() or column_string.lstrip("-").isdigit():
            raise ValueError("Move must be composed of valid string direction values.")
        # Check for correctness of row value
        elif row_string not in row_mapping.keys():
            raise ValueError("Incorrect string direction value for row position.")
        # Check for correctness of column value
        elif column_string not in column_mapping.keys():
            raise ValueError("Incorrect string direction value for column position.")
        # Check if player has already been assigned an id
        elif self.player_id is None:
            raise ValueError("Cannot make a move without assigning a player id.")
        # Check if player has already been assigned an icon
        elif self.player_icon is None:
            raise ValueError("Cannot make a move without assigning a player icon.")

        # Convert the move string into corresponding row and column indices
        row_position = row_mapping[row_string]
        column_position = column_mapping[column_string]

        # Ask the board if the move is valid.
        if not board.is_valid_move(row_position, column_position):
            raise ValueError(f"Cell ({row_position}, {column_position}) is not a valid move.")
        
        # Place the mark on the board.
        board.place_mark(row_position, column_position, self.player_icon)
        
        # Call the make_move function with correct row and column positions
        self._make_move(row_position, column_position)

    def _make_move(self, row_position: int, column_position: int) -> None:
        """
        Internal function. Takes in valid row and column positions. Adds a tuple of 
        (row_position, column_position) to the player's set of moves.
        """

        # Add the move to the set of player moves
        self.player_moves.add((row_position, column_position))
        
        return