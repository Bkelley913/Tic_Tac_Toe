# Function to print the current board state
def print_board(board):
    for row in board:
        print(" | ".join(row)) # Join the elements of the row with "|"
        print("-" * 9) # Print a line of dashes

# Function to check if a player has won
def is_winner(board, player):
    for i in range(3):
        # Check rows and columns for a win
        if board[i][0] == board[i][1] == board[i][2] == player or \
            board[0][i] == board[1][i] == board[2][i] == player:
            return True
        # Check diagonals for a win
        if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

# Function to check if the board is full
def is_full(board):
    for row in board:
        if " " in row: # If there is an empty space, the board is not full
            return False
        return True

# Function to make a move on the board
def make_move(board, row, col, player):
    if board[row][col] == " ": # Check if the spot is empty
        board[row][col] = player
        return True
    else:
        return False

# Function to play the game
def play_game():
    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O")
    print_board(board) # Print initial empty board

    while True:
        print(f"Player {current_player}, make your move (row and column): ")
        move = input().split()
        row, col = int(move[0]), int(move[1])

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid move! Row and column values should be between 0 and 2.")
            continue

        if make_move(board, row, col, current_player):
            print_board(board)

            if is_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if is_full(board):
                print("IT'S A TIE")
                break

            current_player = "O" if current_player == "X" else "X" # Switch Players
        else:
            print("Invalid Move! That spot is already taken.")

# Start the game
play_game()