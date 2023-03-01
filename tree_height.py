# python3

import sys 
import threading

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            if parents[i] not in tree:
                tree[parents[i]] = []
            tree[parents[i]].append(i)
    return dfs(tree, root)

def dfs(tree, node):
    if node not in tree:
        return 1
    heights = [dfs(tree, child) for child in tree[node]]
    return max(heights) + 1

def main():
    filename = input("")
    while 'a' in filename:
        filename = input("Invalid file name. Please enter a different file name: ")
    try:
        with open(filename, 'r') as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
    except FileNotFoundError:
        print("File not found.")
        return
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()



