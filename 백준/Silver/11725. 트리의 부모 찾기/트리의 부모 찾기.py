
import sys

n = int(sys.stdin.readline().rstrip())

# 인접 리스트 초기화
adj_list = {i: [] for i in range(1, n+1)}

# 인접 리스트 만들기  (숫자 넣기)
for i in range(1, n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


# ????왜 N+1인지 visited 초기회
visited = [False for i in range(n+1)]
queue = []

# Store its parent node
ans = {i: 0 for i in range(1, n+1)}


# BFS
def bfs(head):
    # 첫 노드
    visited[head] = True
    queue.append(head)
    while queue:
        vertex = queue.pop(0)
        for neighbor in adj_list[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                ans[neighbor] = vertex
                queue.append(neighbor)


bfs(1)
for i in ans:
    if i ==1:
        continue
    print(ans[i])
