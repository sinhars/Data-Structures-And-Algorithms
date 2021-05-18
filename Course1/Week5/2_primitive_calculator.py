# Uses python3
import sys

def fast_optimal_sequence(n):
    sequences = [0] * n
    for i in range(len(sequences)):
        if i == 0:
            sequences[i] = [1]
        else:
            prev_best = sequences[i - 1]
            if ((i + 1) % 2 == 0):
                option2 = sequences[((i + 1) // 2) - 1] 
                if len(option2) < len(prev_best):
                    prev_best = option2
            if ((i + 1) % 3 == 0):
                option3 = sequences[((i + 1) // 3) - 1] 
                if len(option3) < len(prev_best):
                    prev_best = option3
            curr_seq = prev_best + [i + 1]
            sequences[i] = curr_seq
    return (sequences[-1])

def optimal_sequence(n):
    if n == 1:
        return [1]
    else:
        prev_best = optimal_sequence(n - 1)
        if n % 3 == 0:
            prev_seq_3 = optimal_sequence(n // 3)
            if len(prev_seq_3) < len(prev_best):
                prev_best = prev_seq_3
        if n % 2 == 0:
            prev_seq_2 = optimal_sequence(n // 2)
            if len(prev_seq_2) < len(prev_best):
                prev_best = prev_seq_2
        prev_best.append(n)
        return (prev_best)

def greedy_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    sequence = list(fast_optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
