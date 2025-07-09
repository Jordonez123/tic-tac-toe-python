from tournament import Tournament
from player import PlayerImpl
def print_start_game_decorations():
    print("")
    print("")
    print("Welcome to Tic Tac Toe")
    print("An implementation built from the ground up by Jordan Ordonez Chaguay")
    print("Let's play!")
    print("")
    print("")

def print_end_game_decorations():
    print("")
    print("")
    print("Hope you had fun!")
    print("Thank you for playing!")
    print("")
    print("")

def create_new_tournament(player1: PlayerImpl, player2: PlayerImpl):
    tournament = Tournament(player1, player2)
    return tournament

if __name__ == "__main__":
    print_start_game_decorations()
    player1, player2 = PlayerImpl(""), PlayerImpl("")
    current_tournament = create_new_tournament(player1, player2)
    current_tournament.start_tournament()
    print_end_game_decorations()
