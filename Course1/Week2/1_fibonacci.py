# Uses python3

import sys
import numpy as np

def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_by_sum(n):
    fib_arr = np.zeros(n + 1, dtype=np.longlong)
    for i in range(n + 1):
        fib_arr[i] = i if (i <= 1) else (fib_arr[i - 1] + fib_arr[i - 2])
    fin_n = fib_arr[n]
    return (fin_n)

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(calc_fib_by_sum(n))
