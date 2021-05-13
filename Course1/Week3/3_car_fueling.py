# python3
import sys

def compute_min_refills(distance, tank, stops):
    position = 0
    i = 0
    stop_count = 0
    stops.append(distance)
    while (position + tank) < distance:
        while stops[i] <= (position + tank):
            i += 1
        if (position == stops[i - 1]):
            return -1
        position = stops[i - 1]
        stop_count += 1
    return (stop_count)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
