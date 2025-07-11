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

def print_end_game_decorations(tournament_winner: str, player_scores: dict):
    print("")
    print(f"{tournament_winner} has won the tournament!")
    for player, games_won in player_scores.items():
        print(f"{player} won {games_won} games in the tournament.")
    print("Hope you had fun.")
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
    tournament_winner = current_tournament.get_tournament_winner()
    player_scores = current_tournament.get_player_scores()
    print_end_game_decorations(tournament_winner, player_scores)
