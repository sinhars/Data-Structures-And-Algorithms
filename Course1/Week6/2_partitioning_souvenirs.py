# Uses python3
import sys
import random
import itertools

def fast_partition3(A, verbose=False):
    total = sum(A)
    if (total % 3) == 0 and len(A) >= 3:
        optimal_sum = total // 3 
        all_combos = []
        for i in range(len(A) + 1):
            for combo in itertools.combinations(A, i):
                if sum(combo) == optimal_sum:
                    all_combos.append(list(combo))
        
        A.sort()
        for set in itertools.combinations(all_combos, 3):
            arr_new = []
            for sub_arr in set:
                arr_new += sub_arr
            arr_new.sort()
            if A == arr_new:
                return (1)
    return (0)

def partition3(A):
    if sum(A) % 3 == 0:
        for c in itertools.product(range(3), repeat=len(A)):
            sums = [None] * 3
            for i in range(3):
                sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
            if sums[0] == sums[1] and sums[1] == sums[2]:
                return 1
    return (0)

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
            print("FAILED: Actual answer = %d" % (test1))
            _ = fast_partition3(a_copy, verbose=True)
            break

if __name__ == '__main__':
    # testRandomSamples(count=20, max_val=30)
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # print(partition3(A))
    print(fast_partition3(A, verbose=True))
