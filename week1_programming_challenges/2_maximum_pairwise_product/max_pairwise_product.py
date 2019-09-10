# python3

from random import randrange

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

# 11 9 2 7 3 4 => 99
# 2 3 4 => 12
# 2 8 4 10 13 9 0 => 130
# 2 9 1 0 3 9 => 81
# 100000 900000 => 90000000000
# 1 => 1
# [] => 0
# 1 2 => 2
# 2 1 => 2

# 2 9 1 3 6 4 => 9, 6
# 0 0 0 0 => 0, 0
# 1 1 1 1 => 1, 1
# 2 3 => 3, 2
# 9 2 3 9 4 => 9, 9

def max_pairwise_product_n(numbers):
    n = len(numbers)
    maxVal = -9999999
    maxVal2 = -9999999

    for i in range(0, n):
        if maxVal < numbers[i]:
            maxVal2 = maxVal
            maxVal = numbers[i]
        elif maxVal2 < numbers[i]:
            maxVal2 = numbers[i]

    return maxVal * maxVal2

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    index_1 = 0
    index_2 = 0

    for i in range(1, n):
        if numbers[index_1] < numbers[i]:
            index_1 = i

    if index_1 == 0:
        index_2 = 1
    
    for j in range(1, n):
        if j != index_1 and numbers[index_2] < numbers[j]:
            index_2 = j

    return numbers[index_1] * numbers[index_2]

def max_pairwise_product_bubble(numbers):
    n = len(numbers)

    for i in range(n-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    for i in range(n-2):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    return numbers[n-1] * numbers[n-2]

def max_pairwise_product_sorted(numbers):
    numbers.sort()
    n = len(numbers)

    return numbers[n-1] * numbers[n-2]

if __name__ == '__main__':
    '''while True:
        n = randrange(2, 10000)
        numbers = [randrange(100000) for x in range(n)]
        print(numbers)

        result1 = max_pairwise_product(numbers)
        result2 = max_pairwise_product_n(numbers)

        if result1 != result2:
            print("WRONG")
            break'''

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_n(input_numbers))
