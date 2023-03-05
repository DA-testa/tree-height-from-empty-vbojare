import sys
import threading

def compute_height(n, parents):
    if len(parents) != n:
        raise ValueError("Invalid input: number of parents does not match number of nodes")
    if parents.count(-1) != 1:
        raise ValueError("Invalid input: not a rooted tree")
    if set(parents) - {-1} - set(range(n)):
        raise ValueError("Invalid input: parents contain invalid node index")

    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)

    def compute_height_rec(node):
        if not tree[node]:
            return 1
        return max(compute_height_rec(child) for child in tree[node]) + 1

    return compute_height_rec(parents.index(-1))

 def main():
      if len(sys.argv) > 1:
        filename = sys.argv[1]
        if "a" in filename:
            print("Error: Filename cannot contain the letter 'a'")
            return
        try:
            with open(filename) as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return
      else:
        print("Enter input:")
        n = int(input())
        parents = list(map(int, input().split()))

      try:
        height = compute_height(n, parents)
        print(height)
      except ValueError as e:
        print("Error:", e)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
