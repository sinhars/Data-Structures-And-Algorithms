# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    sum = 0
    current = 0
    next  = 1
    for i in range(n + 1):
        if i >= m:
            sum += current
        current, next = next, current + next
    return sum % 10

def fibonacci_partial_sum_fast(m, n):
    curr_last_digit = 0
    next_last_digit = 1
    sum_last_digit = 0
    for i in range(n + 1):
        if i >= m:
            sum_last_digit = (sum_last_digit + curr_last_digit) % 10
        curr_last_digit, next_last_digit = next_last_digit, (curr_last_digit + next_last_digit) % 10
    return (sum_last_digit)

if __name__ == '__main__':
    input = sys.stdin.readline();
    m, n = map(int, input.split())
    print(fibonacci_partial_sum_fast(m, n))