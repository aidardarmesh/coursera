# Uses python3
import sys

def get_change(m):
    # to get minimum number of coins, we need  divide m
    # to maximum denominations
    # m = 23
    # 23 // 10 = 2, min_coins += 2, 23 % 10 = 3
    # 3 // 5 = 0, min_coins += 0, 3 % 5 = 3
    # 3 // 1 = 3, min_coins += 3, 3 % 1 = 0
    # min_coins = 5
    denoms = [1, 5, 10]
    min_coins = 0
    denoms.sort(reverse=True)

    for divisor in denoms:
        min_coins += m // divisor
        m = m % divisor

    return min_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
