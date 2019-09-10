# Uses python3

# 0 1 2 3 4 5 6  7  8  9 10
# 0 1 1 2 3 5 8 13 21 34 55

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_optimized(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for i in range(n - 1):
        previous, current = current, previous + current
    
    return current

def calc_fib_table(n):
    if n <= 1:
        return n
    
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    
    return f[n]

"""for i in range(11):
    result1 = calc_fib(i)
    result2 = calc_fib_table(i)

    print(result1, result2)

    if result1 != result2:
        print('WRONG')"""

n = int(input())
print(calc_fib_optimized(n))