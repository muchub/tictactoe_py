# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. Players take turns marking spaces in a 3x3 grid with their respective symbols, typically 'X' and 'O', with the goal of getting three of their symbols in a row, column, or diagonal.

## How to Play

1. Run the Python script.
2. Players take turns entering the number corresponding to the position they want to mark.
3. The game ends when one player gets three of their symbols in a row, column, or diagonal, or when all spaces are filled without a winner (a tie).

## Code Explanation

The code consists of a `map()` function to display the current state of the game board, a loop to handle player moves, and logic to check for a winner or a tie. Here's a brief overview:

- The game board is represented as a list of strings.
- Players are represented by 'X' and 'O'.
- The `win_condition` list holds the winning combinations.
- The game loop continues until there's a winner or a tie.

## Running the Code

To run the game:

```bash
python tic_tac_toe.py
