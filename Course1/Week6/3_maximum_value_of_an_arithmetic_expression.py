# Uses python3

import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def print2d(arr):
    for i in range(len(arr)):
        print(arr[i])

def get_min_max(exp_min, exp_max, ops, i, j):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evalt(exp_min[i][k], exp_min[k + 1][j], ops[k])
        b = evalt(exp_max[i][k], exp_min[k + 1][j], ops[k])
        c = evalt(exp_min[i][k], exp_max[k + 1][j], ops[k])
        d = evalt(exp_max[i][k], exp_max[k + 1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return (min_value, max_value)

def get_maximum_value(dataset, verbose=False):    
    expr = [x for x in dataset]
    nums = [int(x) for x in expr[::2]]
    ops = expr[1::2]
    
    exp_min = [[0 for j in range(len(nums))] for i in range(len(nums))]
    exp_max = [[0 for j in range(len(nums))] for i in range(len(nums))]

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                exp_min[i][j] = nums[i]
                exp_max[i][j] = nums[i]
    
    for j in range(1, len(nums)):
        for i in range(len(nums), -1, -1):
            if i < j:
                exp_min[i][j], exp_max[i][j] = get_min_max(exp_min, exp_max, ops, i, j)
    if verbose:
        print2d(exp_min)
        print2d(exp_max)
    return (exp_max[0][-1])


if __name__ == "__main__":
    print(get_maximum_value(input(), verbose=False))