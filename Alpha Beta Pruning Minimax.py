# Create empty board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Check if there is a winner
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Make a move
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

# Optimized Minimax with Alpha-Beta Pruning
def alphabeta(board, depth, is_ai_turn, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_full(board):
        return 0

    if is_ai_turn:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alphabeta(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Alpha-Beta Pruning for Maximizer
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alphabeta(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha-Beta Pruning for Minimizer
        return min_eval

# Find best move for AI using Alpha-Beta
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = alphabeta(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_tictactoe():
    board = create_board()
    current_player = "X"  # Human always starts

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        if current_player == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
        else:
            row, col = best_move(board)
            print(f"AI chooses: {row}, {col}")

        if 0 <= row < 3 and 0 <= col < 3:
            if make_move(board, row, col, current_player):
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already taken.")
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tictactoe()
