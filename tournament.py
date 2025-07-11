import time
import random
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
        # Ask player 1 for name
        player1_name = input("Player 1 Name: ")
        self.player1.name = player1_name

        # Ask player 2 for name
        player2_name = input("Player 2 Name: ")
        self.player2.name = player2_name
    
    def get_player_order(self):
        first_player_order = random.randint(0, 1)
        second_player_order = not first_player_order
        return first_player_order, second_player_order
        
    def _create_new_game(self) -> Game:
        # Create a new board
        new_board = Board()
        # Create a new game and pass in the players and new board
        new_game = Game(self.player1, self.player2, new_board)
        
        # Return the new game
        return new_game

    def _play_single_game(self, game_number: int):
        print(f"|---- Game {game_number}/3 ----|\n")
        clean_game = self._create_new_game()
        self._determine_playing_order()
        self._assign_icons()
        self._announce_playing_order()
        clean_game.play_game()
        self._record_winner(clean_game)

    def _determine_playing_order(self):
        print("")
        first_player_order, second_player_order = self.get_player_order()
        self.player1.set_player_id(first_player_order)
        self.player2.set_player_id(second_player_order)

    def _assign_icons(self):
        self.player1.player_icon = None
        self.player2.player_icon = None
        if self.player1.player_id == 0:
            self.player1.set_player_icon("X")
            self.player2.set_player_icon("O")
        else:
            self.player1.set_player_icon("O")
            self.player2.set_player_icon("X")

    def _announce_playing_order(self):
        print("Determining playing order ...")
        time.sleep(2)
        if self.player1.player_id == 0:
            print(f"{self.player1.name} goes first")
            print(f"{self.player2.name} goes second")
        else:
            print(f"{self.player2.name} goes first")
            print(f"{self.player1.name} goes second")

    def _record_winner(self, game):
        winner = game.get_game_winner()
        if winner:
            self.player_scores[winner.name] += 1

    def _end_tournament(self):
        self.tournament_ended = True
        self.tournament_winner = max(self.player_scores, key=self.player_scores.get)

    def start_tournament(self):
        self.set_up_players()
        print("")
        for i in range(3):
            self._play_single_game(i + 1)
            self._end_tournament()

    def get_tournament_winner(self) -> PlayerImpl:
        return self.tournament_winner
    
    def get_player_scores(self):
        return self.player_scores