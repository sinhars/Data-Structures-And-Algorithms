# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    
    first_max = -1
    first_max_idx = -1
    for i in range(n):
        if(numbers[i] > first_max):
            first_max = numbers[i]
            first_max_idx = i
    
    second_max = -1
    for j in range(n):
        if((j != first_max_idx) & (numbers[j] > second_max)):
            second_max = numbers[j]
    
    max_product = first_max * second_max
    return (max_product)


def max_pairwise_product_clean(numbers):
    numbers.sort(reverse=True)
    max_product = numbers[0] * numbers[1]
    return (max_product)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_clean(input_numbers))
