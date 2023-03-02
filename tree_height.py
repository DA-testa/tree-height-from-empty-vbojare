import sys
import threading

def build_tree(n, parents):
    tree = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    return tree, root

def dfs(node, depth, tree):
    if not tree[node]:
        return depth
    max_depth = depth
    for child in tree[node]:
        max_depth = max(max_depth, dfs(child, depth+1, tree))
    return max_depth

def compute_height(n, parents):
    tree, root = build_tree(n, parents)
    max_height = dfs(root, 1, tree)
    return max_height

def main():
    filename = input("Enter file name: ")
    if 'a' in filename:
        print("Invalid file name")
        return
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
    except FileNotFoundError:
        print("File not found")
        return
    max_height = compute_height(n, parents)
    print(max_height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
