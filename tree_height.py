import sys
import threading

def compute_height(n, parents):
tree = [[] for _ in range(n)]
for child, parent in enumerate(parents):
if parent == -1:
root = child
else:
tree[parent].append(child)
def height(node):
    if not tree[node]:
        return 1
    return 1 + max(height(child) for child in tree[node])

return height(root)
def main():
n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
sys.setrecursionlimit(107) 
threading.stack_size(227) 
threading.Thread(target=main).start()