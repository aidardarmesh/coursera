# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # sort segments according to s.end in ASC order
    # get rightmost point of first segment
    # if point will be in further segments, get rid off them
    # else, get new rightmost point and repeat iteration until the end of segments

    n = len(segments)

    # sorting segments according to 'end' point
    for i in range(n):
        for j in range(i+1, n):
            if segments[i].end > segments[j].end:
                segments[i], segments[j] = segments[j], segments[i]
    
    current_point = segments[0].end
    points.append(current_point)

    for i in range(1, n):
        if segments[i].start <= current_point <= segments[i].end:
            pass
        else:
            current_point = segments[i].end
            points.append(current_point)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
