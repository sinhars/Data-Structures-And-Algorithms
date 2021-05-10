# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current
    return sum % 10

def fibonacci_sum_squares_fast(n):
    if n <= 1:
        return n
    prev_last_digit = 0
    curr_last_digit = 1
    sum_sq_last_digit = 1
    for _ in range(n - 1):
        prev_last_digit, curr_last_digit = curr_last_digit, (prev_last_digit + curr_last_digit) % 10
        sum_sq_last_digit += (curr_last_digit ** 2) % 10
        sum_sq_last_digit %= 10
    return (sum_sq_last_digit)

if __name__ == '__main__':
    n = int(stdin.readline())
    print(fibonacci_sum_squares_fast(n))
