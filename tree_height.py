import sys
import threading

def compute_height(n, parents):
    # Check if the input represents a valid tree
    if len(parents) != n:
        raise ValueError("Invalid input: number of parents does not match number of nodes")
    if parents.count(-1) != 1:
        raise ValueError("Invalid input: not a rooted tree")
    if set(parents) - {-1} - set(range(n)):
        raise ValueError("Invalid input: parents contain invalid node index")

    # Create a list to represent the tree
    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)

    # Recursively compute the height of the tree
    def compute_height_rec(node):
        if not tree[node]:
            return 1
        return max(compute_height_rec(child) for child in tree[node]) + 1

    return compute_height_rec(parents.index(-1))

def main():
    # Check if input is from a file or from keyboard
    if len(sys.argv) > 1:
        # If input is from a file, read input from file
        filename = sys.argv[1]
        if 'a' in filename:
            print("Error: File name should not contain letter 'a'")
            return
        try:
            with open(filename, 'r') as file:
                # Read number of elements
                n = int(file.readline())
                # Read the list of parents
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("Error: File not found")
            return
    else:
        # If input is from keyboard, read input from console
        try:
            n = int(input())
            parents = list(map(int, input().split()))
        except ValueError:
            print("Error: Invalid input")
            return

    # Compute the height of the tree
    try:
        height = compute_height(n, parents)
    except ValueError as e:
        print(str(e))
        return

    # Print the height
    print(height)

# Set the recursion limit and stack size for the new thread
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# Start a new thread for the main function
threading.Thread(target=main).start()
