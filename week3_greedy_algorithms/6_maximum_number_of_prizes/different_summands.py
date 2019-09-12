# Uses python3
import sys

def optimal_summands(n):
    summands = []
    # n=6, counter=1
    # while n > 0:
    # 1 is not in summands => [1], n=5, counter=2
    # 2 is not in summands => [1, 2], n=3, counter=3
    # 3 is not in summads => [1, 2, 3], n=0, counter=4

    # n=8, counter=1
    # while n > 0:
    # 1 is not in summands and n-1(7) is not in summands => [1], counter=2, n=7
    # 2 is not in summands and n-2(5) is not in summands => [1, 2], counter=3, n=5
    # 3 is not in summands and n-3(2) is     in summands => counter=4
    # 4 is not in summands and n-4(1) is     in summands => counter=5
    # 5 is not in summands and n-5(0) is not in summands => [1, 2, 5]

    # n=2, counter=1
    # 1 == n-1(1), counter=2
    # 2 != n-2(0), 2 is not in summands and n-2(0) is not in summands => [2], n=0, counter=3

    # n=1, counter=1
    # 1 != n-1(0), 1 is not in summands and n-1(0) is not in summands => [1], n=0, counter=2

    counter = 1
    n_copy = n

    while n > 0 and counter <= n_copy:
        if counter != n-counter:
            if not counter in summands and not n-counter in summands:
                summands.append(counter)
                n -= counter
        counter += 1

    return summands

def optimal_summands_optimized(n):
    summands = []
    l = 1

    while n > 0:
        if n > 2 * l:
            summands.append(l)
            n -= l
        else:
            summands.append(n)
            n -= n
        l += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands_optimized(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
