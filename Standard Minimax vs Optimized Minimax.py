import time

class TicTacToe:
    def __init__(self):
        self.board = self.init_board()
        self.nodes_visited_standard = 0
        self.nodes_visited_optimized = 0

    def init_board(self):
        return [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def board_is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def find_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def minimax_standard(self, depth, ai_turn):
        self.nodes_visited_standard += 1

        winner = self.find_winner()
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif self.board_is_full():
            return 0

        if ai_turn:
            max_value = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        value = self.minimax_standard(depth + 1, False)
                        self.board[i][j] = " "
                        max_value = max(max_value, value)
            return max_value
        else:
            min_value = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        value = self.minimax_standard(depth + 1, True)
                        self.board[i][j] = " "
                        min_value = min(min_value, value)
            return min_value

    def alphabeta_minimax_optimized(self, depth, ai_turn, alpha, beta):
        self.nodes_visited_optimized += 1

        winner = self.find_winner()
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif self.board_is_full():
            return 0

        if ai_turn:
            max_value = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        value = self.alphabeta_minimax_optimized(depth + 1, False, alpha, beta)
                        self.board[i][j] = " "
                        max_value = max(max_value, value)
                        alpha = max(alpha, value)
                        if beta <= alpha:
                            break
            return max_value
        else:
            min_value = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        value = self.alphabeta_minimax_optimized(depth + 1, True, alpha, beta)
                        self.board[i][j] = " "
                        min_value = min(min_value, value)
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
            return min_value

    def find_best_move_standard(self):
        best_score = -float('inf')
        optimal_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax_standard(0, False)  # Run minimax here to increment nodes visited
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        optimal_move = (i, j)
        return optimal_move

    def find_best_move_optimized(self):
        best_score = -float('inf')
        optimal_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.alphabeta_minimax_optimized(0, False, -float('inf'), float('inf'))
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        optimal_move = (i, j)
        return optimal_move

    def compare_algorithms(self):
        # Timing and comparing the Standard Minimax
        print("\nStandard Minimax Game:")
        self.board = self.init_board()
        start_time = time.time()
        self.find_best_move_standard()  # Running with Standard Minimax
        end_time = time.time()
        standard_time = end_time - start_time
        print(f"Standard Minimax Time: {standard_time:.6f} seconds")
        print(f"Nodes Visited by Standard Minimax: {self.nodes_visited_standard}")

        # Timing and comparing the Alpha-Beta Pruning Optimized Minimax
        print("\nAlpha-Beta Minimax Game:")
        self.board = self.init_board()
        start_time = time.time()
        self.find_best_move_optimized()  # Running with Alpha-Beta Minimax
        end_time = time.time()
        optimized_time = end_time - start_time
        print(f"Alpha-Beta Minimax Time: {optimized_time:.6f} seconds")
        print(f"Nodes Visited by Alpha-Beta Minimax: {self.nodes_visited_optimized}")
        
        # Compare the results
        print("\nComparison Results:")
        print(f"Time Improvement: {standard_time - optimized_time:.6f} seconds")
        print(f"Node Reduction: {self.nodes_visited_standard - self.nodes_visited_optimized} nodes")

    def play_game(self):
        current_player = "X"  # Human is "X", AI is "O"
        while True:
            self.print_board()

            if current_player == "X":
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                except ValueError:
                    print("Please enter valid numbers.")
                    continue
            else:
                row, col = self.find_best_move_standard()  # AI plays with Standard Minimax
                print(f"AI chooses (Standard): {row}, {col}")
                # This is just to simulate the turn, actual play will be done later for Alpha-Beta

            if 0 <= row < 3 and 0 <= col < 3:
                self.board[row][col] = current_player
                winner = self.find_winner()
                if winner:
                    self.print_board()
                    print(f"Player {winner} wins!")
                    break
                elif self.board_is_full():
                    self.print_board()
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToe()

    # Play both games: Standard Minimax and Alpha-Beta Minimax
    game.play_game()  # Standard Minimax is played during the game
    game.compare_algorithms()  # The comparison will be printed after the game
