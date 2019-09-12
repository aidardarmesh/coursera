#Uses python3

import sys

def max_dot_product(a, b):
    # sort a, sort b in DESC orders
    # [1 3 -5] => [3 1 -5]
    # [-2 4 1] => [4 1 -2]
    # 3*4 + 1*1 + (-5)*(-2) = 23
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
