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

def calc_fib_optimized(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1

    for i in range(n-1):
        previous, current = current, previous + current

    return current

def get_fibonacci_huge_optimized(n, m):
    # calculate fn % m
    # append value it to period
    # if half of period is equal to another half, then stop counting fn
    # get reminder n % m = l
    # get f(l) % m
    period = []
    period_len = len(period)

    for i in range(n):
        period.append(calc_fib_optimized(i) % m)
        period_len = len(period)
        
        if period[:period_len] == period[period_len]:
            break
    
    l = n % period_len

    return calc_fib_optimized(l) % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_optimized(n, m))
