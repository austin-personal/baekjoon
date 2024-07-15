import sys
from collections import deque

def dfs(node):
    global cnt
    visited[node] = True
    route.append(node)

    if inOut[node - 1] == 1 and len(route) > 1:  # Found a valid route
        cnt += 1

    for neighbor in adj_dict[node]:
        if not visited[neighbor]:
            if (inOut[node - 1] == 1 and len(route) == 1) or inOut[node - 1] == 0:
                dfs(neighbor)

    route.pop()
    visited[node] = False

# Get number of nodes
n = int(sys.stdin.readline().strip())

# Get in or out data
inOut = list(map(int, sys.stdin.readline().strip()))

# Initialize adj_dict
adj_dict = {i: [] for i in range(1, n + 1)}

# Build adj_dict
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    adj_dict[a].append(b)
    adj_dict[b].append(a)

# Initialize visited array and other variables
visited = [False] * (n + 1)
route = []
cnt = 0

# Perform DFS for each node that could be a starting point
for i in range(1, n + 1):
    if inOut[i - 1] == 1:
        dfs(i)

print(cnt)
