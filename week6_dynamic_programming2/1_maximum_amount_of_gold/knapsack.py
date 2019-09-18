# Uses python3
import sys

def optimal_weight(W, weights):
    n = len(weights)
    values = weights[:] # to be clear with meaning of values and weights

    # initialization
    m = [[0 for i in range(0, W+1)] for j in range(0, n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            m[i][w] = m[i-1][w]

            if weights[i-1] <= w:
                val = m[i-1][w-weights[i-1]] + values[i-1]

                if m[i][w] < val:
                    m[i][w] = val
    
    return m[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
