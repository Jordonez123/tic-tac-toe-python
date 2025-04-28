### Tic Tac Toe Implementation
#### Jordan Israel Ordone Chaguay
#### April 26, 2025

## General Description:
Implementation for a 2 player Tic Tac Toe game played on a 3x3 board.

At the start of the game, the players will have the chance to call either heads or tails and toss a fair 2 sided coin. Whoever wins the coin toss will begin the game. Players take turns making 1 valid move at at time marked by either "X" for player 1 or "O" for player 2. The game will terminate on the turn of the player that completes a set of 3 in the following directions: vertical, horizontal, diagonal.

The game will be played in the best 2 out of 3 (whichever player reaches this first).

### Main Classes
1. Tournament: will keep track of the best of 3 games
2. Game: will keep track of the current game being played
3. Board: responsible to set up the initial 3x3 tic-tac-toe board for each game
4. Player: responsible to keep track of the number of winning games of each player, the current move of each player.

### Class Initialization
#### Tournament
- number_of_games: int
- tournament_ended: boolean
- tournament_winner: int
- player_scores: dict (player_id:score)
- def get_tournament_winner
- def display_tournament_winner

#### Game:
- def __init__(player1, player2, board) 
- def play_game
- def get_game_winner
- def _get_game_captions
- def set_player_order

#### Board:
- board: 2D array initially filled with "?"
- current_turn: int
- display_board
- get_next_move

#### Player
- name: str
- player_id: int
- set_player_id
- def check_if_won
- def make_move


## File Structure:
```
|
|-- __init.py__ 
|
|-- tournament.py
|-- game.py 
|-- board.py
|-- player_abc.py
|-- player.py 
|
|-- tests/
|   |--__init__.py
|   |
|   |-- test_player.py
|   |-- test_board.py
|   |-- test_game.py
|   |-- test_tournament.py
|
|-- main.py
```
## Approach to Testing

This project follows Test-Driven Development (TDD) principles to ensure robust, maintainable, and reliable code.

#### Testing Strategy:

1. **Abstract Base Classes**: I designed abstract base classes where necessary to prevent circular dependencies and promote clean architecture.

2. **Dedicated Test Classes**: Each project class has an associated test class, ensuring isolated and comprehensive testing.

3. **Unit Tests for Each Function**:
- Every method is tested individually, covering both positive (expected) and negative (unexpected) cases.

4. **Testing Checklist for Each Unit Test**:
```
[✅] Handles normal input correctly
[✅] Handles empty or missing input
[✅] Handles wrong or unexpected input
[✅] Correctly handles boundary conditions
[✅] Ensures object state is accurate after operation
```

5. **Development Workflow**:

- Write tests first, ensuring all five scenarios above are covered.

- Implement the function only after test cases are in place.

- Repeat for each function.

- Repeat for each class.