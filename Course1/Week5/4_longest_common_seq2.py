#Uses python3

import sys

def lcs2(a, b):
    d = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    for i in range(1, len(d)):
        for j in range(1, len(d[0])):
            is_same = 1 if (a[i - 1] == b[j - 1]) else 0 
            d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1] + is_same)
    # for i in range(len(d)):
    #     print(d[i][:])
    return (d[-1][-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
