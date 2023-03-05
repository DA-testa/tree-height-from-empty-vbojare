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
    print("Select input source:")
    print("1. Keyboard")
    print("2. File")
    source = input()

    if source == "2":
        filename = input("Enter file name: ")
        
        if 'a' in filename:
            print("Error: File name should not contain letter 'a'")
            return
        
        try:
            with open(filename, 'r') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("Error: File not found")
            return
    else:
        try:
            n = int(input("Enter number of elements: "))
            parents_str = input("Enter the list of parents separated by space: ")
            parents = list(map(int, parents_str.split()))
        except ValueError:
            print("Error: Invalid input")
            return

    height = compute_height(n, parents)
    print(height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
