# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

# n    = 0 1 2 3 4 5  6  7  8  9  10
# F(n) = 0 1 1 2 3 5  8  13 21 34 55
# S(n) = 0 1 2 4 7 12 20 33 54 88 143

# from_ = 3, to = 7: F(7) + F(6) + F(5) + F(4) + F(3)
# S(7) = |F(7) + F(6) + F(5) + F(4) + F(3)| + F(2) + F(1) + F(0)
# S(2) =                                      F(2) + F(1) + F(0)
# l = l(S(7)) - l(S(2)) = l(33) - l(2) = (3 - 2) % 10 = 1

# from = 10, to = 10: F(10)
# l = l(S(10)) - l(S(9)) = l(143) - l(88) = (3 - 8) % 10 = 5

def fib_sum_last(n):
    if n <= 1:
        return n
    
    # S(n) = F(n+2) - 1 (FACT)
    n += 2
    previous = 0
    current = 1
    # F(n) % m, where m >= 2, reminder has period (FACT)
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
    last = (period[reminder] - 1) % 10

    return last

def fibonacci_partial_sum_optimized(from_, to):
    S_to = fib_sum_last(to)
    S_from = 0

    if from_ > 0:
        S_from = fib_sum_last(from_-1)

    return (S_to - S_from) % 10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_optimized(from_, to))