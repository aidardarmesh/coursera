# python3
import sys

def compute_min_refills(distance, tank, stops):
    stops.append(distance) # [200, 375, 550, 750, 950]
    left = 0
    refills = 0
    right = left + tank
    n = len(stops)
    stations = []
    i = 0

    while i < n:
        if stops[i] <= right:
            stations.append(stops[i])
            i += 1
        else:
            if len(stations) == 0:
                return -1
            left = stations.pop()
            refills += 1
            right = left + tank

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
