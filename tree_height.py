# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height
    tree = {}
    root = None 
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent] =[i]

    def compute_subtree_height(node):
        if node not in tree:
            return 1
        subtree_heights = [compute_subtree_height(child)for child in tree[node]]
        return max(subtree_heights) +1
     
    return compute_subtree_height(root)


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    n = int(input())
    parents = list(map(int,input().split()))

    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

