# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (right+left) // 2

    left_m = get_majority_element(a, left, mid)
    right_m = get_majority_element(a, mid, right)

    left_count = 0

    for i in range(left, right):
        if left_m == a[i]:
            left_count += 1

    if left_count > (right-left) // 2:
        return left_m
    
    right_count = 0

    for i in range(left, right):
        if right_m == a[i]:
            right_count += 1
    
    if right_count > (right-left) // 2:
        return right_m

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
