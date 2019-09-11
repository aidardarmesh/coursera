# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_optimized(n):
    # F(1)^2 + F(2)^2 + F(3)^2 + F(4)^2 = F(4) * F(5)
    # get F(4) and F(5) by periods
    # return F(4) * F(5) % 10
    if n <= 1:
        return n
    
    n += 1
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
    prelast = period[reminder-1]

    return prelast * last % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_optimized(n))
