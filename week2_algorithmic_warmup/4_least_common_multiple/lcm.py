# Uses python3
from random import randrange
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# 6 8 => 24
# 17 3 => 51
# 8 1 => 8
# 111 296 => 888

def gcd(a, b):
    larger = max(a, b)
    smaller = min(a, b)

    while True:
        reminder = larger % smaller

        if reminder == 0:
            break
        else:
            larger, smaller = smaller, reminder

    return smaller

def lcm_optimized(a, b):
    if a == 0 or b == 0: # min value is 1 according to the problem desc, but test failed
        return 0
    return a*b // gcd(a, b)

if __name__ == '__main__':
    """for i in range(100):
        a = randrange(1, 1000)
        b = randrange(1, 1000)
        print(a, b)

        result1 = lcm_naive(a, b)
        result2 = lcm_optimized(a, b)

        print(result1, result2)

        if result1 != result2:
            print('WRONG')
            break"""
        
    a, b = map(int, input().split())
    print(lcm_optimized(a, b))