import unittest
from board import Board

class TestBoard(unittest.TestCase):

    # -------------------------- Set Up and Tear Down ------------------------------------

    def setUp(self):
        # Runs before each test case
        # Creates fresh board for the each new game
        self.board = Board()

    def tearDown(self):
        # Runs after each test case
        # Deletes the board object created during setUp
        self.board = None

    # -------------------------- Displays ------------------------------------

    def test_display_initial_board(self):
        """
        Checks if we have a 3 x 3 board initially filled with
        "?"s.
        """
        valid = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != "?":
                    valid = False
        
        self.assertTrue(valid)
    
    def test_display_board(self):
        """
        Test out the __str__ method for the board class
        """
        test_board = "? | ? | ?\n? | ? | ?\n? | ? | ?"
        self.assertEqual(test_board, str(self.board))
    
    # -------------------------- Update board ------------------------------------
    def test_place_mark(self):
        pass
    # -------------------------- Board Utilities ------------------------------------
    def test_reset_(self):
        pass

    def test_get_empty_cells(self):
        pass

    def test_is_full(self):
        pass

    def test_copy(self):
        pass

    def test_undo_move(self):
        pass
    # -------------------------- Valid Moves ------------------------------------
    def test_is_valid_move(self):
        pass
    # -------------------------- Winner Checks ------------------------------------
    def test_check_winner(self):
        pass

    # -------------------------- Game State ------------------------------------
    def test_current_game_state(self):
        pass

    def test_is_game_over(self):
        pass



if __name__ == "__main__":
    unittest.main()