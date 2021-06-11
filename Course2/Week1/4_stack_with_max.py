#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        curr_max = a if (len(self.__max_stack) == 0) else self.__max_stack[len(self.__max_stack) - 1]
        if a >= curr_max:
            self.__max_stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[len(self.__stack) - 1] == self.__max_stack[len(self.__max_stack) - 1]:
            self.__max_stack.pop()
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return (self.__max_stack[len(self.__max_stack) - 1])


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
