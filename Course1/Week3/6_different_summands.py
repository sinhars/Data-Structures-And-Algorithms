# Uses python3
import sys
import math

def optimal_summands(n):
    summands = []
    k = math.floor((math.sqrt(8 * n + 1) - 1) / 2)
    for x in range(k - 1):
        summands.append(x + 1)
        n -= (x + 1)
    if (n > 0):
        summands.append(n)

    return summands

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
