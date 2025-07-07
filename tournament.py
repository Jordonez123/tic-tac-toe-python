from game import Game
from player import PlayerImpl
from board import Board
from collections import defaultdict

class Tournament:
    def __init__(self, player1: PlayerImpl, player2: PlayerImpl):
        self.number_of_games = None
        self.tournament_ended = False
        self.tournament_winner = None
        self.player1 = player1
        self.player2 = player2
        self.player_scores = defaultdict(int) # {name: score}

    def set_up_players(self) -> None:
        # Ask player 1 for name and assign playing order
        player1_name = input("Player 1 Name: ")
        self.player1.set_player_id(0)
        self.player1.name = player1_name
        # Ask player 2 for name and assign playing order
        player2_name = input("Player 2 Name: ")
        self.player2.set_player_id(1)
        self.player2.name = player2_name
        # Assign icons "X" or "O" for player 1 and player respectively
        self.player1.set_player_icon("X")
        self.player2.set_player_icon("O")

    def _create_new_game(self) -> Game:
        # Create a new board
        new_board = Board()
        # Create a new game and pass in the players and new board
        new_game = Game(self.player1, self.player2, new_board)
        
        # Return the new game
        return new_game
    
    def start_tournament(self):
        # Get a new game
        clean_game = self._create_new_game()
        
        # Main loop, for a tournament of 3 games
        for _ in range(3):
            # Play the game
            clean_game.play_game()
            # Get the winner
            winner = clean_game.get_game_winner
            

        

    def get_tournament_winner(self) -> PlayerImpl:
        return self.tournament_winner
    
    def display_tournament_winner(self) -> str:
        pass
