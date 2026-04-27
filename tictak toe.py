# Tic Tac Toe Game

# Create the board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check for a win
def check_win(player):
    # All winning combinations
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a tie
def check_tie():
    return " " not in board

# Main game loop
current_player = "X"
game_running = True

print("Welcome to Tic Tac Toe!")
display_board()

while game_running:
    print("\nPlayer", current_player)
    move = int(input("Choose a position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
        display_board()

        if check_win(current_player):
            print("\nPlayer", current_player, "wins!")
            game_running = False
        elif check_tie():
            print("\nIt's a tie!")
            game_running = False
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
    else:
        print("That spot is already taken. Try again.")
