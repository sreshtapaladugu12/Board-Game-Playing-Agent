# Import required modules
from dataclasses import dataclass
from typing import List
from collections import deque
import heapq
import math
import random

# Board size
ROWS = 6
COLS = 7


# ---------------- CO1 ----------------
# Agent Model, State Representation, Actions, Transition

@dataclass
class State:
    board: List[List[str]]


class ConnectFour:

    def __init__(self):
        self.board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

    def display(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def valid_actions(self):
        return [c for c in range(COLS) if self.board[0][c] == '.']

    def transition(self, col, piece):
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == '.':
                self.board[row][col] = piece
                return True
        return False


# ---------------- CO2 ----------------
graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('C', 2)],
    'B': [('D', 1)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 5,
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'G': 0
}


def bfs(start):
    q = deque([start])
    visited = set()

    print("\nBFS Traversal:")

    while q:
        node = q.popleft()
        print(node, end=" ")
        visited.add(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)


def dfs(start):
    stack = [start]
    visited = set()

    print("\nDFS Traversal:")

    while stack:
        node = stack.pop()
        print(node, end=" ")
        visited.add(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


def ucs(start, goal):
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return cost

        for neighbor, w in graph[node]:
            heapq.heappush(pq, (cost + w, neighbor))


def astar(start, goal):
    pq = [(heuristic[start], 0, start)]

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            return g

        for neighbor, w in graph[node]:
            heapq.heappush(
                pq,
                (g + w + heuristic[neighbor], g + w, neighbor)
            )


# ---------------- CO3 ----------------
class CSP:

    def __init__(self, board):
        self.board = board

    def forward_check(self):
        return [c for c in range(COLS) if self.board[0][c] == '.']

    def mrv(self):
        return min(self.forward_check())

    def degree(self):
        return max(self.forward_check())

    def lcv(self):
        return max(self.forward_check())

    def valid(self, col):
        if col not in self.forward_check():
            print("Constraint Failed")
            return False
        return True


# ---------------- CO4 ----------------
def evaluate():
    return random.randint(1, 10)


def minimax(depth, maximizing):

    if depth == 0:
        return evaluate()

    if maximizing:
        best = -math.inf

        for _ in range(2):
            best = max(best, minimax(depth - 1, False))

        return best

    else:
        best = math.inf

        for _ in range(2):
            best = min(best, minimax(depth - 1, True))

        return best


def alphabeta(depth, alpha, beta, maximizing):

    if depth == 0:
        return evaluate()

    if maximizing:

        value = -math.inf

        for _ in range(2):
            value = max(
                value,
                alphabeta(depth - 1, alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for _ in range(2):
            value = min(
                value,
                alphabeta(depth - 1, alpha, beta, True)
            )

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


# ---------------- CO5 ----------------
def bayes(prior, likelihood, evidence):
    return (likelihood * prior) / evidence


transition_matrix = {
    1: [0.2, 0.3, 0.5],
    2: [0.4, 0.4, 0.2],
    3: [0.3, 0.5, 0.2]
}


def predict_next_move(current_move):
    probabilities = transition_matrix[current_move]

    next_move = probabilities.index(
        max(probabilities)
    ) + 1

    return next_move


def expected_utility(utility, probability):
    return utility * probability


# ---------------- CO6 ----------------
class HybridAgent:

    def __init__(self, game):
        self.game = game

    def choose_move(self):

        best_move = None
        best_score = -1

        csp = CSP(self.game.board)

        for move in self.game.valid_actions():

            if csp.valid(move):

                utility_score = alphabeta(
                    3,
                    -math.inf,
                    math.inf,
                    True
                )

                probability = bayes(
                    0.4,
                    random.uniform(0.5, 0.9),
                    0.5
                )

                score = expected_utility(
                    utility_score,
                    probability
                )

                print(
                    f"Column {move+1} -> "
                    f"Utility={utility_score}, "
                    f"Probability={round(probability,2)}, "
                    f"Expected Utility={round(score,2)}"
                )

                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move


# ---------------- MAIN PROGRAM ----------------
game = ConnectFour()
agent = HybridAgent(game)

print("CONNECT FOUR AI AGENT")
print("Human = X | AI = O")

bfs('S')
dfs('S')

print("\nUCS Cost:", ucs('S', 'G'))
print("A* Cost:", astar('S', 'G'))

while True:

    game.display()

    col = int(input("Enter column (1-7): ")) - 1

    if col in game.valid_actions():

        game.transition(col, 'X')

        ai_col = agent.choose_move()

        print("\nAI chooses column", ai_col + 1)

        game.transition(ai_col, 'O')

    else:
        print("Invalid Move")
