# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

        def create_tree(self, parents, verbose=False):
                root = None
                children = [None] * self.n
                for i in range(self.n):
                        if parents[i] == -1:
                                root = i
                        else:
                                if children[parents[i]] is None:
                                        children[parents[i]] = [i]
                                else:
                                        children[parents[i]] += [i]
                if verbose:
                        print(root, children)
                return (root, children)

        def read(self, verbose=False):
                self.n = int(sys.stdin.readline())
                self.parents = list(map(int, sys.stdin.readline().split()))
                self.root, self.children = self.create_tree(self.parents, verbose=verbose)

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parents[i]
                        maxHeight = max(maxHeight, height)
                return (maxHeight)

        def compute_height_fast(self, node_index=-1):
                if node_index == -1:
                        node_index = self.root
                children = self.children[node_index]
                if children is None:
                        return 1
                else:
                        max_height = -1
                        for child in children:
                                height = self.compute_height_fast(node_index=child)
                                max_height = max(max_height, height)
                        return (max_height + 1)
                
def main():
        tree = TreeHeight()
        tree.read(verbose=False)
        # print(tree.compute_height())
        print(tree.compute_height_fast())

threading.Thread(target=main).start()
