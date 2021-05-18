#Uses python3

import sys

def lcs3(a, b, c):
    d = [[[0 for i in range(len(c) + 1)] for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    for i in range(1, len(d)):
        for j in range(1, len(d[0])):
            for k in range(1, len(d[0][0])):
                is_same = 1 if (a[i - 1] == b[j - 1] == c[k - 1]) else 0 
                d[i][j][k] = max(d[i-1][j][k], d[i][j-1][k], d[i][j][k-1], \
                    d[i-1][j-1][k], d[i-1][j][k-1], d[i][j-1][k-1], d[i-1][j-1][k-1] + is_same)
    return (d[-1][-1][-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
