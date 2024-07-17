import sys
from collections import deque

input = sys.stdin.read
data = input().split()

n, m, k, x = map(int, data[:4])

# 인접 리스트 초기화
adj_dict = {i: [] for i in range(1, n + 1)}

# 간선 입력 받아서 인접 리스트 채우기
index = 4
for i in range(m):
    a, b = int(data[index]), int(data[index + 1])
    adj_dict[a].append(b)
    index += 2

# BFS 함수 정의
def bfs(start_node):
    visited = [False] * (n + 1)
    queue = deque([start_node])
    visited[start_node] = True
    distance = 0
    result = []

    while queue:
        if distance == k:
            result.extend(queue)
            break
        for _ in range(len(queue)):
            v = queue.popleft()
            for neighbor in adj_dict[v]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        distance += 1

    if distance < k or not result:
        return [-1]
    else:
        return sorted(result)

# 결과 출력
result = bfs(x)
for city in result:
    print(city)
