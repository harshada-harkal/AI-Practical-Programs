#Alpha-Beta Pruning

import math

values = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, index, maxPlayer, alpha, beta):

    if depth == 3:
        return values[index]

    if maxPlayer:
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth+1, index*2+i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(depth+1, index*2+i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

    return best

result = alphabeta(0, 0, True, -math.inf, math.inf)

print("Optimal Value:", result)
