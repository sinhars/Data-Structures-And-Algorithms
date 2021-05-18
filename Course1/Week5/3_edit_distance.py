# Uses python3

def edit_distance(s, t):
    d = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    for i in range(len(d)):
        d[i][0] = i
    for j in range(len(d[0])):
        d[0][j] = j
    for i in range(1, len(d)):
        for j in range(1, len(d[0])):
            diag = 0 if (s[i - 1] == t[j - 1]) else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + diag)
    
    # for i in range(len(d)):
    #     print(d[i][:])
    
    return (d[-1][-1])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
