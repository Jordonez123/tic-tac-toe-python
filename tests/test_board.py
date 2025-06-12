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
        self.board.place_mark(0, 0, "X")
        self.board.place_mark(1, 1, "O")
        self.board.place_mark(2, 2, "X")
        test_board = "X | ? | ?\n? | O | ?\n? | ? | X"
        
        self.assertEqual(str(self.board), test_board)
    
    def test_cannot_place_invalid_mark(self):
        invalid_mark = ":)"
        
        with self.assertRaises(ValueError) as context:
            self.board.place_mark(0, 0,invalid_mark)
            
        self.assertEqual(str(context.exception), "Cannot use an invalid mark on the board.")
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
        """
        Tests a correct move (within bounds and on an empty cell).
        """
        # all of the cells in self.board are empty (contain '?') on setUp.
        
        # define the test move
        test_move = (0, 0)

        self.assertTrue(self.board.is_valid_move(test_move[0], test_move[1]))

    def test_is_not_valid_move_filled_cell(self):
        """
        Tests an incorrect move (on a filled cell).
        """
        # mark a cell on self.board as filled
        self.board.place_mark(0, 0, "X")

        # define the test move on the same marked row and column above
        test_move = (0, 0)

        self.assertFalse(self.board.is_valid_move(test_move[0], test_move[1]))

    def test_is_not_valid_move_oob(self):
        """
        Tests an incorrect move (out of bounds).
        """
        # define list of test moves to be outside the 3 x 3 board
        # row index, column index
        test_moves = [(-1, -1), (4, 4), (7, -2), (float("-inf"), float("inf"))]

        for row, col in test_moves:
            self.assertFalse(self.board.is_valid_move(row, col), f"Assertion failed for test case: ({row, col})")
    
    # -------------------------- Winner Checks ------------------------------------
    def test_check_winner_X(self):
        """
        Test that correct winner is displayed.
        Test for X.
        """

        # X should win in this scenario
        self.board.place_mark(0, 0, "X")
        self.board.place_mark(0, 1, "X")
        self.board.place_mark(0, 2, "X")
        self.board.place_mark(1, 1, "O")
        self.board.place_mark(2, 2, "O")

        # print out the board
        print("")
        print("---- X wins example: ----")
        print(self.board)
        print("")

        self.assertEqual(self.board.check_winner(), "X")

    def test_check_winner_O(self):
        """
        Test that correct winner is displayed.
        Test for O.
        """
        # O should win in this scenario
        self.board.place_mark(0, 0, "O")
        self.board.place_mark(0, 1, "O")
        self.board.place_mark(0, 2, "O")
        self.board.place_mark(1, 1, "X")
        self.board.place_mark(2, 2, "X")

        # print out the board
        print("")
        print("---- O wins example: ----")
        print(self.board)
        print("")

        self.assertEqual(self.board.check_winner(), "O")

    def test_check_winner_Draw(self):
        """
        Test that no winner is displayed (Game has come to a draw).
        """

        # should return None in this scenario
        marks = ["O", "X", "O", "X", "X", "O", "X", "O", "X"]
        
        # track current mark position
        position_mark = 0

        # fill in the board
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board.place_mark(i, j, marks[position_mark])
                position_mark += 1
        
        self.assertEqual(self.board.check_winner(), None)
        
        # print out the board
        print("")
        print("---- Draw example: ----")
        print(self.board)
        print("")

        self.assertEqual(self.board.check_winner(), None)

    def test_check_winner_in_progress(self):
        """
        Test that no winner is displayed (Game is still in progress).
        """

        # should return None in this scenario

        self.board.place_mark(0, 0, "X")
        self.board.place_mark(1, 1, "O")
        self.board.place_mark(2, 2, "X")
        self.board.place_mark(1, 0, "O")

        # print out the board
        print("")
        print("---- Winner in progress example: ----")
        print(self.board)
        print("")

        self.assertEqual(self.board.check_winner(), None)
    # -------------------------- Game State ------------------------------------
    def test_current_game_state_won(self):
        """
        Game state is returned as "X wins or O wins."
        """
        pass

    def test_current_game_state_draw(self):
        """
        Game state is returned as "Draw."
        """
        pass

    def test_current_game_state_in_progress(self):
        """
        Game state is returned as "In Progress."
        """
        pass

    def test_is_game_over_won(self):
        """
        Test if current game has concluded. Check when someone has won.
        """
        pass

    def test_is_game_over_board_full(self):
        """
        Test if current game has concluded. Check when all the cells in the
        3 x 3 board are filled.
        """
        pass



if __name__ == "__main__":
    unittest.main()