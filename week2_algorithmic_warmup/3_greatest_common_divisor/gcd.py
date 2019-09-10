# Uses python3

from random import randrange

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# 12 6 = 6   6 12 = 6 => 12 % 6 = 0 => 6
# 17 3 = 1   3 17 = 1 => 17 % 3 = 2, 3 % 2 = 1, 2 % 1 = 0
# 900 2 = 2  2 900 = 2 => 900 % 2 = 0 => 2
# 42 35 = 7  35 42 = 7
# 8 1 = 1    1 8 = 1

def gcd_optimized(a, b):
    # Euclidian algorithm:
    # define larger and smaller
    # remainder = larger % smaller
    # if remainder == 0: return smaller
    # else: larger = smaller, smaller = reminder
    larger = max(a, b)
    smaller = min(a, b)

    while True:
        reminder = larger % smaller
        
        if reminder == 0:
            break
        else:
            larger, smaller = smaller, reminder
    
    return smaller

if __name__ == "__main__":
    """for i in range(100):
        a = randrange(1, 1000)
        b = randrange(1, 1000)

        result1 = gcd_naive(a, b)
        result2 = gcd_optimized(a, b)

        print(a, b, result1, result2)

        if result1 != result2:
            print('WRONG')
            break"""

    a, b = map(int, input().split())
    print(gcd_optimized(a, b))
