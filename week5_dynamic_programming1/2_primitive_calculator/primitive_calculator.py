# Uses python3
import sys

def optimal_sequence(n):
    min_opers = {1:0}
    connectors = {1:0}
    elems = []
    infinity = 99999999

    for i in range(2, n+1):
        min_opers[i] = infinity

        for case in range(3, 0, -1):
            prev = -1
            opers = infinity

            if case == 3:
                if i % 3 == 0:
                    prev = i//3
                    opers = min_opers[prev] + 1
            elif case == 2:
                if i % 2 == 0:
                    prev = i//2
                    opers = min_opers[prev] + 1
            else:
                prev = i-1
                opers = min_opers[prev] + 1

            if opers < min_opers[i]:
                min_opers[i] = opers
                connectors[i] = prev

    while n != 0:
        elems.append(n)
        n = connectors[n]

    elems.reverse()

    return elems

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')