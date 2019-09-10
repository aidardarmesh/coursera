# Uses python3

# 0 1 2 3 4 5 6  7  8  9 10 11  12  13  14
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_optimized(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10

if __name__ == '__main__':
    """for i in range(10000):
        result1 = get_fibonacci_last_digit_naive(i)
        result2 = get_fibonacci_last_digit_optimized(i)

        print(result1, result2)

        if result1 != result2:
            print('WRONG')
            break"""
    
    n = int(input())
    print(get_fibonacci_last_digit_optimized(n))