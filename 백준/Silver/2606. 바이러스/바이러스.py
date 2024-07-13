# 입력 처리
import sys
input = sys.stdin.read
data = input().strip().split()

# 컴퓨터 수와 네트워크 연결 수 입력
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

# DFS 함수 정의 (재귀적 구현)
def dfs(node):
    d_visited[node] = True
    for neighbor in li[node]:
        if not d_visited[neighbor]:
            dfs(neighbor)

# 1번 컴퓨터에서 DFS 시작
dfs(1)

# 1번 컴퓨터를 제외한 웜 바이러스에 걸린 컴퓨터의 수를 계산
infected_computers = sum(d_visited) - 1

# 결과 출력
print(infected_computers)
