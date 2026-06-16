import math
import random

def evaluate():
    return random.randint(1,10)

def minimax(depth, maximizing):

    if depth == 0:
        return evaluate()

    if maximizing:
        best = -math.inf

        for _ in range(2):
            best = max(best,minimax(depth-1,False))

        return best

    else:
        best = math.inf

        for _ in range(2):
            best = min(best,minimax(depth-1,True))

        return best

def alphabeta(depth, alpha, beta, maximizing):

    if depth == 0:
        return evaluate()

    if maximizing:
        value = -math.inf

        for _ in range(2):
            value = max(
                value,
                alphabeta(depth-1,alpha,beta,False)
            )

            alpha = max(alpha,value)

            if alpha >= beta:
                break

        return value

    else:
        value = math.inf

        for _ in range(2):
            value = min(
                value,
                alphabeta(depth-1,alpha,beta,True)
            )

            beta = min(beta,value)

            if beta <= alpha:
                break

        return value