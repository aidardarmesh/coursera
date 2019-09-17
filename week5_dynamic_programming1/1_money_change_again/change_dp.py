# Uses python3
import sys

def get_change(money):
    coins = [1, 3, 4]
    min_num_coins = [0]
    infinity = 9999999999

    for money_val in range(1, money+1):
        min_num_coins.append(infinity)

        for coin in coins:
            if money_val >= coin:
                num_coins = min_num_coins[money_val-coin] + 1

                if num_coins < min_num_coins[money_val]:
                    min_num_coins[money_val] = num_coins

    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))