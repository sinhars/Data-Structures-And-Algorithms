# Uses python3
import sys
from collections import namedtuple
from numpy.core.fromnumeric import sort

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    sorted_segments = sorted(segments , key=lambda x: x.start, reverse=False)
    while len(sorted_segments) > 0:
        min_end = min([x.end for x in sorted_segments])
        while (len(sorted_segments) > 0) and (sorted_segments[0].start <= min_end):
            sorted_segments.pop(0)
        points.append(min_end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
