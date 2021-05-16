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

def fibonacci_sum_faster(n):
    if n < 0:
        return (0)
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

def fibonacci_partial_sum_faster(m, n):
    sum_m = fibonacci_sum_faster(m - 1)
    sum_n = fibonacci_sum_faster(n)
    partial_sum = sum_n - sum_m
    if(partial_sum < 0):
        partial_sum += 10
    return (partial_sum)

if __name__ == '__main__':
    input = sys.stdin.readline();
    m, n = map(int, input.split())
    print(fibonacci_partial_sum_faster(m, n))