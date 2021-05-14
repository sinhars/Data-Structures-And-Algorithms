# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return (-1)
    elif left + 1 == right:
        return (a[left])
    mid = (left + right) // 2
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid, right)
    left_count = 0
    right_count = 0
    for i in range(left, right):
        if a[i] == left_majority:
            left_count += 1
        elif a[i] == right_majority:
            right_count += 1
    if left_count > (right - left) / 2:
        return (left_majority)
    elif right_count > (right - left) / 2:
        return (right_majority)
    return (-1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
