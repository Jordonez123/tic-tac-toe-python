import unittest
from player import PlayerImpl

class TestPlayer(unittest.TestCase):

    # -------------------------- Set Up and Tear Down ------------------------------------

    def setUp(self):
        # Runs before each test case
        # Creates fresh player1 and player2 instances
        self.player1 = PlayerImpl("Jordan")
        self.player2 = PlayerImpl("Jennifer")
    
    def tearDown(self):
        # Runs after each test case
        # sets both player1 and player2 instances to None
        self.player1 = None
        self.player2 = None
    
    # -------------------------- Player Instance Variables ------------------------------------
    
    def test_player_initialization(self):
        self.assertEqual(self.player1.name, "Jordan")
        self.assertEqual(self.player2.name, "Jennifer")
    
    def test_cannot_override_player_id(self):
        # Come up with move original move order
        original_move_order = 0
        new_move_order = 1

        # Assign original player ID
        self.player1.set_player_id(original_move_order)

        # Try to overwrite. Should raise a ValueError Exception
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_id(new_move_order)

        self.assertEqual(str(context.exception), "Cannot overwrite previosuly assigned player ID.")

    def test_cannot_set_none_player_id(self):
        # Assign a None value to move order
        move_order = None
        
        # Expecting a ValueError to be raised
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_id(move_order)
        
        self.assertEqual(str(context.exception), "Cannot assign an empty or NULL player ID.")
    
    def test_cannot_set_nonbinary_player_id(self):
        # Assign a non-binary move order
        move_order = 3

        # Expecting a ValueError to be raised
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_id(move_order)
        
        self.assertEqual(str(context.exception), "Player ID cannot be set to a non-binary value.")
    
    def test_set_player_id(self):
        # Come up with move order
        move_order = 0

        # Assign move order to player
        self.player1.set_player_id(move_order)

        # Check that the move order was correctly assigned
        self.assertEqual(self.player1.player_id, move_order,
                         f"Player move order: {move_order} not successfully assigned.")
    
    # -------------------------- Player Icon ------------------------------------
    
    def test_set_player_icon(self):
        # Icon mapping
        icon_mapping = {"X": 0, "O": 1}

        # Set the player IDs

        self.player1.set_player_id(1)
        self.player2.set_player_id(0)

        # Generate "X" and "O" icons for the players
        player1_icon = "O"
        player2_icon = "X"

        # Set the icon for each player
        self.player1.set_player_icon(player1_icon)
        self.player2.set_player_icon(player2_icon)

        # Check that the icons for each player match their respective player IDs.
        self.assertEqual(icon_mapping[self.player1.player_icon], self.player1.player_id,
                         f"Player 1 icon: {self.player1.player_icon} does not correspond to player id: {self.player1.player_id}")
        self.assertEqual(icon_mapping[self.player2.player_icon], self.player2.player_id, 
                         f"Player 2 icon: {self.player2.player_icon} does not correspond to player id: {self.player2.player_id}")
        
        # Check that the icons for each player have been correctly assigned 
    
    def test_cannot_set_none_player_icon(self):
        # Set the player ID
        self.player1.set_player_id(0)

        # Assign a None value to the player icon
        player_icon = None

        # Expecting a ValueError to be raised
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_icon(player_icon)
        
        self.assertEqual(str(context.exception), "Player icon cannot be set to None or Empty.")
    
    def test_cannot_overwrite_player_icon(self):
        # Set the player ID
        self.player1.set_player_id(0)
        
        # Create original and new icons to test
        original_icon = "X"
        new_icon = "O"

        # Assign the original icon to player
        self.player1.set_player_icon(original_icon)
        
        # Expecting a ValueError when attempting to overwrite original player icon
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_icon(new_icon)

        self.assertEqual(str(context.exception), f"Player already has an icon: {self.player1.player_icon}")

    def test_cannot_assign_icon_without_player_id(self):
        # Create a player icon
        player_icon = "X"

        # Expecting a ValueError when attempting to assign a player icon
        # Without first assigning a valid player ID
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_icon(player_icon)
        
        self.assertEqual(str(context.exception), "The player must have a valid player ID before attempting to assign a player icon.")

    def test_cannot_assign_invalid_player_icon(self):
        # Create an invalid icon
        player_icon = ":)"

        # Assign player ID for testing
        self.player1.set_player_id(0)

        # Expecting ValueError exception when attempting to assign invalid player icon
        with self.assertRaises(ValueError) as context:
            self.player1.set_player_icon(player_icon)
        
        self.assertEqual(str(context.exception), "Invalid Player icon assignment. Must assign a player icon of either X or O.")

    # -------------------------- Player Moves ------------------------------------
    
    def test_player_cannot_make_nondirectional_move(self):
        # Assign player id
        self.player1.set_player_id(0)

        # Assign player icon to the created player above
        self.player1.set_player_icon("X")

        # create a list of invalid non-directional player moves
        non_valid_moves = [
            ((["ajjkjn", 0, 456, {"a": 1}], {1:0}), "Move must be composed of valid string direction values."),
            (("left", "middle"), "Incorrect string direction value for row position."),
            (("top", "bottom"), "Incorrect string direction value for column position."),
            (("12345", "middle"), "Move must be composed of valid string direction values."), # testing positive digit
            (("middle", "-1902"), "Move must be composed of valid string direction values."), # testing negative digit
            ((None, "left"), "Move must not have None values for either row or column directions."), # testing for None row value
            (("bottom", None), "Move must not have None values for either row or column directions.") # testing for None column value
        ]

        for move, expected_message in non_valid_moves:
            with self.subTest(bad_id=move):
                # Expecting a Value Error exception for each invalid move
                with self.assertRaises(ValueError) as context:
                    self.player1.make_move(move)
                self.assertEqual(str(context.exception), expected_message)

    def test_player_cannot_make_move_without_id_assignment(self):
        # Player move that will be attempted
        player_move = ("bottom", "left")

        # Expecting a ValueError Exception when attempting to make move without assigning an id to player.
        with self.assertRaises(ValueError) as context:
            self.player1.make_move(player_move)
        
        self.assertEqual(str(context.exception), "Cannot make a move without assigning a player id.")
        
    def test_player_cannot_make_move_without_icon_assigned(self):
        # Assign player id
        self.player1.set_player_id(0)

        # Player move that will be attempted
        player_move = ("bottom", "left")

        # Expecting a ValueError Exception when attempting to make move
        # Without assigning the player an icon
        with self.assertRaises(ValueError) as context:
            self.player1.make_move(player_move)
        
        self.assertEqual(str(context.exception), "Cannot make a move without assigning a player icon.")

    def test_player_make_move(self):
        # Creating a valid move
        player_move = ("bottom", "middle")

        # Assigning a valid player id
        self.player1.set_player_id(0)

        # Assigning a valid player icon
        self.player1.set_player_icon("O")

        self.player1.make_move(player_move)
        

        player1_move_positions = (2, 1)

        # Check if player1 and player2 move positions are correctly recorded
        self.assertIn(player1_move_positions, self.player1.player_moves, 
                        f"Player 1 move: {player1_move_positions} not found in {self.player1.player_moves}")

        print("")
        print(f"Player 1 moves: {self.player1.player_moves}")

    # -------------------------- Won A Game on Turn ------------------------------------
    
    def test_player_won_game_on_turn(self):
        # Assign  player id, icon
        self.player1.set_player_id(0)
        self.player1.set_player_icon("X")
        self.player1.player_moves = {()}
if __name__ == "__main__":
    unittest.main()
