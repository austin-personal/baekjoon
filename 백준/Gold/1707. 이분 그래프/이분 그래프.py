import sys
from collections import deque

# Reading the number of test cases
noOfCase = int(sys.stdin.readline())

def bfs(start, adj_dict, visited, check):
    queue = deque([start])
    visited[start] = True
    check[start] = 1  # Start node check value as 1

    while queue:
        node = queue.popleft()
        for neighbor in adj_dict[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                check[neighbor] = -check[node]  # Alternate check value between -1 and 1
            elif check[neighbor] == check[node]:
                return False
    return True

results = []

# Iterate as much as noOfCase
for _ in range(noOfCase):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj_dict = {i: [] for i in range(1, v+1)}

    # Get edges
    for _ in range(e):
        n1, n2 = map(int, sys.stdin.readline().rstrip().split())
        adj_dict[n1].append(n2)
        adj_dict[n2].append(n1)

    visited = [False] * (v + 1)
    check = [0] * (v + 1)
    is_bipartite = True

    # As the graph might be disconnected, we need to check each component
    for i in range(1, v + 1):
        if not visited[i]:
            if not bfs(i, adj_dict, visited, check):
                is_bipartite = False
                break

    if is_bipartite:
        results.append("YES")
    else:
        results.append("NO")

# Print all results
for result in results:
    print(result)
