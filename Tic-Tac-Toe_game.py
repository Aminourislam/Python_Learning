"""
Tic-Tac-Toe Game
----------------
Literally, for this game I had three days of stress.//By the way this is 
a simple Tic-Tac-Toe game where the user plays as 'X' and the computer as 'O'.
The board is displayed after each move, and the game ends when a player wins
or the board is full (draw).
"""

import random
board = [x for x in range(1, 10)]

def display_board():
    print("+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")
    for i in range(0, 9, 3):
        print("|" + "     " + "|" + "     " + "|" + "     " + "|")
        print(f"|  {board[i]}  |  {board[i+1]}  |  {board[i+2]}  |")
        print("|" + "     " + "|" + "     " + "|" + "     " + "|")
        print("+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")

def user_input():
    while True:
        try:
            cell = int(input("Which cell do you want? (1-9): "))
            if cell < 1 or cell > 9:
                print("Please enter a number between 1 and 9.")
                continue
            if isinstance(board[cell - 1], int):
                board[cell - 1] = "X"
                break
            else:
                print("This cell is already taken. Choose another.")
        except ValueError:
            print("Invalid input. Enter a number.")

def computer_choice():
    while True:
        cell = random.randint(1, 9)
        if isinstance(board[cell - 1], int):
            board[cell - 1] = "O"
            break

def check_winner():
    win_patterns = [
	[0,1,2], [3,4,5], [6,7,8],
	[0,3,6], [1,4,7], [2,5,8],
	[0,4,8], [2,4,6]
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] and not isinstance(board[a], int):
            winner = board[a]
            if winner == "X":
                print("You win!")
            else:
                print("Computer wins!")
            return winner
    return None

def is_draw():
    return all(not isinstance(cell, int) for cell in board)

# Gameing code start 
print("Welcome to Tic-Tac-Toe! You are X, computer is O.")
display_board()
print("Computer chooses the center (5).")
board[4] = "O"
display_board()
while True:
    user_input()
    display_board()
    winner = check_winner()
    if winner:
        break
    if is_draw():
        print("It's a draw!")
        break

    print("Computer's turn:")
    computer_choice()
    display_board()
    winner = check_winner()
    if winner:
        break
    if is_draw():
        print("It's a draw!")
        break