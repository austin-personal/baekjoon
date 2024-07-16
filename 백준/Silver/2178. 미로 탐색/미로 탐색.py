import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 1:
                    queue.append((next_x, next_y))
                    graph[next_x][next_y] = graph[x][y] + 1


bfs(0, 0)
print(graph[n - 1][m - 1])
