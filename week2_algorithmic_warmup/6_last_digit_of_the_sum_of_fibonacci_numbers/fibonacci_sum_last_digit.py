# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_optimized(n):
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    for i in range(n-1):
        previous, current = current, (previous + current + 1) % 10
    
    return current

if __name__ == '__main__':
    
    n = int(input())
    print(fibonacci_sum_optimized(n))
