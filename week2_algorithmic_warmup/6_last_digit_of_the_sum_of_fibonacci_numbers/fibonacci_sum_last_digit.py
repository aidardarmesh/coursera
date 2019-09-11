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

# n    = 0 1 2 3 4 5  6  7  8  9  10
# F(n) = 0 1 1 2 3 5  8  13 21 34 55
# S(n) = 0 1 2 4 7 12 20 33 54 88 143
# S(n) = F(n+2)-1

def fibonacci_sum_optimized(n):
    # iterate n+2 times to get F(n+2) % 10 trying to find period
    # get reminder from period list at position n % len(period)
    if n <= 1:
        return n
    
    n += 2
    previous = 0
    current = 1
    period = [0, 1]
    counter = 2

    for i in range(n-1):
        previous, current = current, (previous + current) % 10
        period.append(current)
        counter += 1
        half = counter // 2

        if period[:half] == period[half:]:
            period = period[:half]
            break

    reminder = n % len(period)
    last = period[reminder]

    if last == 0: # last digit can't be negative
        return 9
    
    return last-1

if __name__ == '__main__':
    """for i in range(1000):
        result1 = fibonacci_sum_naive(i)
        result2 = fibonacci_sum_optimized(i)
        print(i, result1, result2)

        if result1 != result2:
            print('WRONG')
            break"""

    n = int(input())
    print(fibonacci_sum_optimized(n))
