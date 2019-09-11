# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_optimized(n, m):
    # calculate fn % m and append to period list
    # if half of period is equal to another half, then stop counting fn
    # l = len(period) // 2
    # calculate reminder = n % l
    # get element period[reminder]
    if n <= 1:
        return n % m
    
    period = [0, 1]
    counter = 2
    previous = 0
    current = 1

    for i in range(n-1):
        previous, current = current, (previous + current) % m
        period.append(current % m)
        counter += 1
        half = counter // 2

        if period[:half] == period[half:]:
            period = period[:half]
            break

    reminder = n % len(period)
    
    return period[reminder]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_optimized(n, m))
