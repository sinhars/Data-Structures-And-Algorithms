# Uses python3
import sys

def computeMid(left, right):
    return ((left + right) // 2)

def binary_search(a, x):
    left, right = 0, (len(a) - 1)
    mid = computeMid(left, right)
    while (a[mid] != x):
        if a[mid] < x:
            left = mid + 1
            mid = computeMid(left, right)
        elif a[mid] > x:
            right = mid - 1
            mid = computeMid(left, right)
        if (left > right) or (mid < 0) or (mid >= len(a)):
            return -1
    return (mid)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = " ")