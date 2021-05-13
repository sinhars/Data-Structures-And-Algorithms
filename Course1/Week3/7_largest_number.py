#Uses python3

import sys
import functools
import random

def compare_numbers(x, y):
    combo1 = int(str(x) + str(y))
    combo2 = int(str(y) + str(x))
    return (combo2 - combo1)
        
def largest_number(a):
    sorted_a = sorted(a, key=functools.cmp_to_key(compare_numbers))
    res = "".join(sorted_a)
    return res

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number_alt(a):
    answer = []
    while a != []:
        max_digit = 0
        for digit in a:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        a.remove(max_digit)
    res = ''.join(answer)
    return (res)

def test_random_samples():
    while True:
        a = []
        n = random.randint(1, 100)
        for _ in range(n):
            a.append(str(random.randint(1, 1000)))
        print(len(a), a)
        test1 = largest_number(a)
        test2 = largest_number_alt(a)
        if(test1 != test2):
            print("FAILED")
            break

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))


    
