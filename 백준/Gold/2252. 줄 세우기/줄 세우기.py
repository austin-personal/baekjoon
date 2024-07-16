import sys
from collections import deque

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])

# in-degree 리스트 초기화
inDegree = {i: 0 for i in range(1, n+1)}

# 인접 리스트 초기화 (Out-degree 만)
adj_dict = {i: [] for i in range(1, n+1)}

# 리스트 들 만들기
index = 2
for i in range(m):
    a, b = int(data[index]), int(data[index+1])
    adj_dict[a].append(b)
    inDegree[b] += 1
    index += 2

# Queue to store temporally node which does not have in-degree node
queue = deque()
ans = []

# function
def line_up():
    # 최초에 in-degree 가 0인 노드들
    for key, nodeValue in inDegree.items():
        if nodeValue == 0:
            queue.append(key)

    while queue:
        v = queue.popleft()
        ans.append(v)

        # v의 인접 리스트 들의 in-degree number 업데이트
        for neighbor in adj_dict[v]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)

line_up()
print(" ".join(map(str, ans)))
