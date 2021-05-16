# Uses python3
import sys
import math

def get_change(m):
    coins = [10, 5, 1]
    total = 0
    for c in coins:
        count = math.floor(m / c)
        m -= (c * count)
        total += count
        if m <= 0:
            break
    return (total)

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
