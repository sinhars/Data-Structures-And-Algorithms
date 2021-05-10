# Uses python3

import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    prev_last_digit = 0
    curr_last_digit = 1
    sum_last_digit = (prev_last_digit + curr_last_digit) % 10
    for _ in range(n - 1):
        prev_last_digit, curr_last_digit = curr_last_digit, (prev_last_digit + curr_last_digit) % 10
        sum_last_digit = (sum_last_digit + curr_last_digit) % 10
    return (sum_last_digit)


def fibonacci_sum_faster(n):
    for i in range(n):
        print(i, fibonacci_sum_fast(i))

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_faster(n))
