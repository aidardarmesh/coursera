#Uses python3

def edit_distance(s1, s2):
    # initialization
    len_s1 = len(s1)
    len_s2 = len(s2)
    d = [[0 for i in range(0, len_s1+1)] for j in range(0, len_s2+1)]
    
    for i in range(1, len_s1+1):
        d[0][i] = i

    for j in range(1, len_s2+1):
        d[j][0] = j

    # filling with min operations
    for i in range(1, len_s2+1):
        for j in range(1, len_s1+1):
            insertion = d[i][j-1] + 1
            deletion  = d[i-1][j] + 1
            match     = d[i-1][j-1]
            mismatch  = d[i-1][j-1] + 1

            if s1[j-1] == s2[i-1]:
                d[i][j] = min(min(insertion, deletion), match)
            else:
                d[i][j] = min(min(insertion, deletion), mismatch)

    # counting edit distance
    i, j, min_distance = len_s2, len_s1, 0

    while i >= 0 and j >= 0:
        if i == 0 and j == 0:
            min_distance += 0
        if i > 0 and d[i][j] == d[i-1][j] + 1: # deletion
            i -= 1
            min_distance += 1
        elif j > 0 and d[i][j] == d[i][j-1] + 1: # insertion
            j -= 1
            min_distance += 1
        elif i > 0 and j > 0 and d[i][j] == d[i-1][j-1] + 1: # mismatch
            i -= 1
            j -= 1
            min_distance += 1
        else: # match
            i -= 1
            j -= 1

    return min_distance

if __name__ == "__main__":
    print(edit_distance(input(), input()))
