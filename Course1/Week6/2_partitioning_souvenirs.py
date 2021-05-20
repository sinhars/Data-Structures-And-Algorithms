# Uses python3
import sys
import random
import itertools

def get_items_used(sum_map, optimal_sum, verbose=False):
    items_used = []
    weight_idx = optimal_sum
    for x in range(len(sum_map) - 1, 0, -1):
        item = A[x - 1]
        if sum_map[x - 1][weight_idx] == sum_map[x][weight_idx]:
            pass
        else:
            items_used.append(A[x - 1]) # Change to x - 1 if indices required instead of items
            weight_idx -= item
        if weight_idx <= 0:
            break
    if verbose:
        print([A[x] for x in items_used])
    
    # Reverse sort if items to be removed from original array
    # items_used.sort(reverse=True)
    
    return (items_used)

def fast_partition3(A, verbose=False):
    total = sum(A)
    A.sort()
    if total % 3 == 0:
        sum_map = [[0 for _ in range(total + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(sum_map)):
            item = A[i - 1]
            for j in range(1, len(sum_map[0])):
                sum_map[i][j] = sum_map[i - 1][j]
                if item <= j:
                    new_val = sum_map[i - 1][j - item] + item
                    if new_val > sum_map[i][j]:
                        sum_map[i][j] = new_val
        if verbose:
            for i in range(len(sum_map)):
                print(sum_map[i])

    return 0

def partition3(A):
    if sum(A) % 3 == 0:
        for c in itertools.product(range(3), repeat=len(A)):
            sums = [None] * 3
            for i in range(3):
                sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

            if sums[0] == sums[1] and sums[1] == sums[2]:
                return 1
    return 0

def testRandomSamples(count, max_val):
    while True:
        a = []
        n = random.randint(1, count)
        for _ in range(n):
            a.append(random.randint(1, max_val))
        print(len(a), a)
        a_copy = [i for i in a]
        test1 = partition3(a)
        test2 = fast_partition3(a, verbose=False)
        if(test1 != test2):
            print("FAILED")
            retest = fast_partition3(a_copy, verbose=True)
            print(retest)
            break

if __name__ == '__main__':
    # testRandomSamples(count=20, max_val=20)
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(fast_partition3(A, verbose=True))
