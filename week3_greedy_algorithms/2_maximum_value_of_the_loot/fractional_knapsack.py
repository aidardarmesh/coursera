# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # capacity = 50, weights = [20, 50, 30], values = [60, 100, 120]
    # vw1 = 60/20 = 3, vw2 = 100/50 = 2, vw3 = 120/30 = 4
    # loop in DESC order: vw3, vw1, vw2
    # while capacity > 0:
    # value += min(capacity, w3) * (v3 / w3)
    # capacity -= w3
    # 
    # value += min(50, 30) * (120 / 30) = 120
    # capacity = 50 - 30 = 20
    # 
    # value += min(20, 20) * (60 / 20) = 60
    # capacity = 20 - 20 = 0
    # find a way to organize values according to the v/w

    # capacity = 10, weights = [30], values = [500]
    # value += min(10, 30) * (500 / 30) = 166.6667
    # capacity = 10 - 30 = -20

    # capacity = 1000, weights = [30], values = [500]
    # value += min(1000, 30) * (500 / 30) = 500
    # capacity = 1000 - 30

    # capacity = 0 => 0.0000

    # capacity = 10, weights = [101], values = [0]
    # value = 0.0000

    # capacity = 10, weights = [101], values = [1]
    # value = 0.0990

    # capacity = 100, weights = [2000000], values = [2000000]
    # value = 100.0000

    value = 0
    vws = []
    n = len(weights)

    for i in range(n):
        vws.append(values[i]/weights[i])

    for i in range(n):
        if capacity == 0:
            return value

        max_index = 0

        for i in range(1, len(vws)):
            if vws[max_index] < vws[i]:
                max_index = i

        weight = min(capacity, weights[max_index])
        value += weight / weights[max_index] * values[max_index]
        capacity -= weight
        weights[max_index] -= weight
        vws[max_index] = 0.0

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
