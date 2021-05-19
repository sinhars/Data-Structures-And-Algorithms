# Uses python3
import sys

def optimal_weight(W, w):
    res = [[0 for j in range(W + 1)] for i in range(len(w) + 1)]
    for i in range(1, len(res)):
        w_i = w[i - 1]
        for j in range(1, len(res[0])):
            res[i][j] = res[i - 1][j]
            if w_i <= j:
                v = res[i - 1][j - w_i] + w_i
                if res[i][j] < v:
                    res[i][j] = v
    
    # for i in range(len(res)):
    #     print(res[i])
    
    result = res[-1][-1]
    return (result)

def greedy_weight(W, w):
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # print(greedy_weight(W, w))
    print(optimal_weight(W, w))
