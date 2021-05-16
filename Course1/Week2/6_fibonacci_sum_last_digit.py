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
    all_fib_last = []
    all_sums = []
    full_pattern = False
    for i in range(n + 1):
        last_ = i if (i <= 1) else ((all_fib_last[i-1] + all_fib_last[i-2]) % 10)
        sum_ = i if (i <= 1) else ((all_sums[i-1] + last_) % 10)
        all_fib_last.append(last_)
        all_sums.append(sum_)
        if (i >= 2) & (all_sums[i - 1] == 0) & (all_sums[i] == 1):
            full_pattern = True
            break
    sum_last_digits = None
    if full_pattern:
        all_sums.pop()
        all_sums.pop()
        pos = n % len(all_sums)
        sum_last_digits = all_sums[pos]
    else:
        sum_last_digits = all_sums[len(all_sums) - 1]
    return (sum_last_digits)   

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_faster(n))
