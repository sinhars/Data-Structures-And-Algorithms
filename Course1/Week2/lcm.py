# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_fast(a, b):
    x = max(a, b)
    for l in range(x, a*b + 1, x):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

