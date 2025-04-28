import unittest
from player import PlayerImpl

class TestPlayer(unittest.TestCase):

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

    """
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


    def test_player_make_move(self):
        # testing a valid move for now, will circle back later
        player1_move, player2_move = ("bottom", "middle"), ("top", "middle")

        self.player1.make_move(player1_move)
        self.player2.make_move(player2_move)

        player1_move_positions, player2_move_positions = (2, 1), (0, 1)

        # Check if player1 and player2 move positions are correctly recorded
        self.assertTrue(player1_move_positions in self.player1.player_moves, 
                        f"Player 1 move: {player1_move_positions} not found in {self.player1.player_moves}")
        self.assertTrue(player2_move_positions in self.player2.player_moves, 
                        f"Player 2 move: {player2_move_positions} not found in {self.player2.player_moves}")

        print("")
        print(f"Player 1 moves: {self.player1.player_moves}")
        print(f"Player 2 moves: {self.player2.player_moves}")

    
    
    
    
    """

if __name__ == "__main__":
    unittest.main()
