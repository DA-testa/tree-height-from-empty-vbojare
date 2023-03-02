def compute_height(n, parents):
    
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj_list[parents[i]].append(i)

    
    def dfs(node):
        heights = []
        for child in adj_list[node]:
            heights.append(dfs(child))
        if not heights:
            return 0
        return max(heights) + 1

    return dfs(root)



try:
    n = int(input())
    parents = list(map(int, input().split()))
    assert len(parents) == n
    assert all(p == -1 or 0 <= p < n for p in parents)
except:
    print('Invalid input')
    exit()


print(compute_height(n, parents))


filename = input('Enter file name: ')
if 'a' in filename:
    print('Invalid file name')
else:
    try:
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            assert len(parents) == n
            assert all(p == -1 or 0 <= p < n for p in parents)
    except:
        print('Invalid file')
        exit()

    print(compute_height(n, parents))
