from player_abc import Player

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
            raise ValueError(f"Cannot overwrite previosuly assigned player ID.")
            
    def set_player_icon(self, icon: str):
        # Check that player ID is already set
        if self.player_id is not None:
            # Player icon has not been set already
            if not self.player_icon:
                self.player_icon = icon
            # Player icon has been set, attempting invalid overriding
            else:
                raise ValueError(f"Player {1 if self.player_id == 0 else 2} already has an icon: {self.player_icon}")
        else:
            raise ValueError(f"The player must have a valid player ID before attempting to assign a player icon.")


    def check_if_won(self):
        pass

    def make_move(self, move: tuple) -> None:
        """move will consist of a tuple of strings in 
        ["left", "middle", "right", "top", "bottom"]
        move = (x, y)
        Where x is either top, middle, or bottom row.
        This corresponds to row indices 0,1,2.
        where y is either left, middle, or right row.
        This corresponds to column indices of 0,1,2.


        Function takes in a VALID MOVE (logic for checking valid is
        in another function).

        """
        row_mapping = {"top": 0, "middle": 1, "bottom": 2}
        column_mapping = {"left": 1, "middle": 1, "right": 2}

        row_string, column_string = move

        # Convert the move string into corresponding row and column indices
        row_position = row_mapping[row_string]
        column_position = column_mapping[column_string]

        if row_position is None or column_position is None:
            raise ValueError(f"Invalid move: {move}. Please check the row and column values.")

        # Add the move to the set of player moves
        self.player_moves.add((row_position, column_position))
        
        return