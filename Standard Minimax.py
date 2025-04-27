# using Minmax Algorithm  
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def find_winner(board):
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

def place_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def minimax_algo(board, depth, is_maximizing):
    winner = find_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax_algo(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax_algo(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def ai_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax_algo(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def start_game():
    board = init_board()
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        if current_player == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
        else:
            row, col = ai_best_move(board)
            print(f"AI chooses: {row}, {col}")

        if 0 <= row < 3 and 0 <= col < 3:
            if place_move(board, row, col, current_player):
                winner = find_winner(board)
                if winner:
                    display_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif board_full(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already taken.")
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    start_game()
