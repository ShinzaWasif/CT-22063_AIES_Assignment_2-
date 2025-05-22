The repository contains codes for Standard Minimax, Alpha Beta Pruning Minimax Algorithms and Comparsion for the best moves of both algorithms.

**Youtube Video Link:**
https://youtu.be/-Ts6sLMqN6Q

**Standard Minimax**
The Standard Minimax algorithm is a decision-making process used to find the optimal move by exploring all possible future game states. It assumes both players play optimally. In games like Tic-Tac-Toe, the algorithm evaluates all potential moves and selects the one that maximizes the player's chances of winning. However, it can be slow for larger game trees since it checks every possible move.

**Optimized Minimax (Alpha-Beta Pruning)**
The Optimized Minimax algorithm improves on Standard Minimax by implementing Alpha-Beta Pruning. This optimization eliminates unnecessary branches from the search tree, improving performance by reducing the number of nodes evaluated. The algorithm keeps track of two values, Alpha and Beta, to stop exploring paths that cannot affect the outcome, making it faster and more efficient, especially in deeper search spaces.

**Comparison Code (Standard Minimax vs Optimized Minimax)**
In the Comparison Code, both the Standard Minimax and the Optimized Alpha-Beta Pruning Minimax are used to simulate the same game scenarios.

The purpose of this comparison is to measure:
Execution Time: How fast each algorithm reaches a decision
Nodes Visited: How many possible game states (nodes) each algorithm evaluated

By running both algorithms under identical conditions, the comparison highlights the efficiency gain offered by Alpha-Beta Pruning.

**By Syeda Shinza Wasif (CT-22063)**
