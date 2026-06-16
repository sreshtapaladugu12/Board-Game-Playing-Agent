import math
import random

from CO1_Agent_Model import ConnectFour
from CO3_CSP import CSP
from CO4_Minimax import alphabeta
from CO5_Bayes import bayes, expected_utility

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
                    random.uniform(0.5,0.9),
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


game = ConnectFour()
agent = HybridAgent(game)

game.display()

col = int(input("Enter column (1-7): ")) - 1

if col in game.valid_actions():

    game.transition(col,'X')

    ai_col = agent.choose_move()

    print("\nAI chooses column", ai_col+1)

    game.transition(ai_col,'O')

game.display()