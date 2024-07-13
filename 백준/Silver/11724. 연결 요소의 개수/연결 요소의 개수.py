import sys
input = sys.stdin.read

# 입력 처리
data = input().strip().split()
v = int(data[0])
e = int(data[1])

# 인접 리스트 초기화
li = {i: [] for i in range(1, v + 1)}

# 간선 정보 입력 및 인접 리스트 구성
index = 2
for _ in range(e):
    n1 = int(data[index])
    n2 = int(data[index + 1])
    li[n1].append(n2)
    li[n2].append(n1)
    index += 2

# 방문 여부 리스트 초기화
d_visited = [False] * (v + 1)

# DFS 함수 정의 (스택 사용)
def dfs(node):
    stack = [node]
    while stack:
        vertex = stack.pop()
        if not d_visited[vertex]:
            d_visited[vertex] = True
            for neighbor in sorted(li[vertex], reverse=True):
                if not d_visited[neighbor]:
                    stack.append(neighbor)

# 연결 요소 개수 세기
cnt = 0
for i in range(1, v + 1):
    if not d_visited[i]:
        dfs(i)
        cnt += 1

# 연결 요소 개수 출력
print(cnt)
