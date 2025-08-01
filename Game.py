import random
import time

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f" {i}  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("   -----------")
    print()  # Extra newline for better readability

# Check for winner
def check_winner(board, player):
    # Rows, Columns, and Diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def play_game():
    print("\nWelcome to Tic Tac Toe! Let's go :-)\n")
    display_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if row in range(3) and col in range(3) and board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers only.")

        print("\nYour Move:")
        display_board(board)

        if check_winner(board, "X"):
            print("You win! :-D")
            break
        if is_board_full(board):
            print("It's a draw :-|")
            break

        # Computer move
        print("Computer is thinking...\n")
        time.sleep(1)  # Add a realistic pause

        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == " ":
                board[row][col] = "O"
                break

        print("Computer's Move:")
        display_board(board)

        if check_winner(board, "O"):
            print("Computer wins! :-(")
            break
        if is_board_full(board):
            print("It's a draw :-|")
            break

        print("-" * 30)  # Visual separator between rounds

# Start the game
play_game()
