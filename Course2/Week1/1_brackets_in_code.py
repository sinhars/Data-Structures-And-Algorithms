# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            if len(opening_brackets_stack) > 0:
                prev = opening_brackets_stack[len(opening_brackets_stack) - 1]
                if are_matching(prev.char, next):
                    opening_brackets_stack.pop()
                else:
                    return (i + 1)
            else:
                return(i + 1)
            pass
    
    if len(opening_brackets_stack) > 0:
        return (opening_brackets_stack[len(opening_brackets_stack) - 1].position + 1)

    return ("Success")

if __name__ == "__main__":
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
