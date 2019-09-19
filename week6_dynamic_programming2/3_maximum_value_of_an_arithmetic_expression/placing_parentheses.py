# Uses python3
import re

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(m, M, ops, i, j):
    min_val = 9999999
    max_val = -9999999

    for k in range(i, j):
        MM = evalt(M[i][k], M[k+1][j], ops[k])
        Mm = evalt(M[i][k], m[k+1][j], ops[k])
        mM = evalt(m[i][k], M[k+1][j], ops[k])
        mm = evalt(m[i][k], m[k+1][j], ops[k])

        min_val = min(min_val, MM, Mm, mM, mm)
        max_val = max(max_val, MM, Mm, mM, mm)

    return min_val, max_val

def get_maximum_value(dgs, ops):
    # digits from str-s to int-s
    dgs = [int(x) for x in dgs]

    # to start counting from 1
    dgs.insert(0, 0)
    ops.insert(0, 0)

    # allocating space
    n = len(dgs)
    m = [[0 for i in range(0, n)] for j in range(0, n)]
    M = [[0 for i in range(0, n)] for j in range(0, n)]

    # initialization of min and max tables
    for i in range(1, n):
        m[i][i], M[i][i] = dgs[i], dgs[i]

    for s in range(1, n-1):
        for i in range(1, n-s):
            j = i + s
            m[i][j], M[i][j] = min_max(m, M, ops, i, j)

    return M[1][n-1]


if __name__ == "__main__":
    expr = input()
    dgs = re.findall('[0-9.]', expr)
    ops = re.findall('[+\-*]', expr)
    print(get_maximum_value(dgs, ops))
