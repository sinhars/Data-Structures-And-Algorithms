# Uses python3
import sys

def get_number_of_inversions(a, left, right):
    b = []
    number_of_inversions = 0
    if left >= right:
        pass
    elif (right - left) == 1:
        b.append(a[left])
    else:
        mid = (left + right) // 2
        b_left, i_left = get_number_of_inversions(a, left, mid)
        b_right, i_right = get_number_of_inversions(a, mid, right)
        number_of_inversions += i_left + i_right
        while len(b_left) > 0 and len(b_right) > 0:
            if b_left[0] <= b_right[0]:
                b.append(b_left[0])
                b_left.pop(0)
            else:
                b.append(b_right[0])
                b_right.pop(0)
                number_of_inversions += len(b_left)
        while len(b_left) > 0:
            b.append(b_left[0])
            b_left.pop(0)
        while len(b_right) > 0:
            b.append(b_right[0])
            b_right.pop(0)
    return (b, number_of_inversions)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b, number_of_inversions = get_number_of_inversions(a, 0, len(a))
    print(number_of_inversions)
