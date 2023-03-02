import sys
import threading


def compute_height(n, parents):
    
    heights = [0] * n
   
    for i in range(n):
     
        height = 1
        
        j = i
        while parents[j] != -1:
      
            if heights[parents[j]] != 0:
                height += heights[parents[j]]
                break
     
            height += 1
            j = parents[j]
        
        heights[i] = height
    
    return max(heights)


def main():
    
    while True:
        file_name = input("Enter the input file name (without 'a'): ")
        if 'a' not in file_name:
            break
        print("Invalid file name. Please try again.")

    with open(file_name, 'r') as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))
 
    height = compute_height(n, parents)
   
    print("Height of the tree:", height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of a bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get a stack of such size
threading.Thread(target=main).start()
