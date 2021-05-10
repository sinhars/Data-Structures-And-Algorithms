# Uses python3
import sys
import numpy as np

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def get_fibonacci_mod(n, m):
    fib_arr = []
    mod_arr = []
    full_pattern = False
    for i in range(n + 1):
        fib = i if (i <= 1) else (fib_arr[i - 1] + fib_arr[i - 2])
        mod = fib % m
        fib_arr.append(fib)
        mod_arr.append(mod)
        if (i >= 2) & (mod_arr[i - 1] == 0) & (mod_arr[i] == 1):
            full_pattern = True
            break
    
    fib_mod = 0
    if full_pattern:
        mod_arr.pop()
        mod_arr.pop()
        pos = n % len(mod_arr)
        fib_mod = mod_arr[pos]
    else:
        fib_mod = fib_arr[len(fib_arr) - 1] % m
    return (fib_mod)

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_mod(n, m))
