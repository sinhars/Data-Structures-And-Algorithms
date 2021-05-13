# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_values = [i / j for i, j in zip(values, weights)]
    data = zip(*[weights, values, unit_values])
    sorted_data = sorted(data , key=lambda x: x[2], reverse=True)
    for i in range(len(sorted_data)):
        item_weight = min(sorted_data[i][0], capacity)
        value += sorted_data[i][2] * item_weight
        capacity -= item_weight
        if (capacity <= 0):
            break
    return (value)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
