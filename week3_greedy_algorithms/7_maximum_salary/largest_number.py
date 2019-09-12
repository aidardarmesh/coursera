#Uses python3

import sys

def is_greater_or_equal(a, b):
    return a + b >= b + a

def largest_number(digits):
    res = ""
    
    while len(digits) > 0:
        max_digit = '0'

        for digit in digits:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        
        res += max_digit
        digits.remove(max_digit)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
