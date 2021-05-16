# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts.sort()
    ends.sort()
    for p in range(len(points)):
        points[p] = [p, points[p]]
    points.sort(key=lambda x:x[1])

    for i in range(len(points)):
        added = 0
        while (len(starts) > 0) and (points[i][1] >= starts[0]):
            added += 1
            starts.pop(0)
        removed = 0
        while (len(ends) > 0) and (points[i][1] > ends[0]):
            removed += 1
            ends.pop(0)
        cnt[points[i][0]] = (cnt[points[i - 1][0]] if i > 0 else 0) + (added - removed)
    
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
