v,e,s = map(int,input().split())

li = {i: [] for i in range(1, v + 1)} # 부모들을 차례대로 넣어 둔다 with []


for _ in range(e):
  n1, n2 = map(int, input().split())
  li[n1].append(n2)
  li[n2].append(n1)

d_ans=[]
d_visited = [False for i in range(v)]
stack = []

def dfs(node):
  stack = [node]
  while stack:
      vertex = stack.pop()
      if not d_visited[vertex - 1]:
          d_visited[vertex - 1] = True
          d_ans.append(vertex)
          # 인접 정점들을 스택에 추가할 때 내림차순으로 정렬하여 작은 번호부터 방문
          for neighbor in sorted(li[vertex], reverse=True):
              if not d_visited[neighbor - 1]:
                  stack.append(neighbor)


b_ans = []
b_visited = [False for i in range(v)]
queue = []

def bfs(node):
  b_visited[node-1] = True
  queue.append(node)
  while queue:
    vertex = queue.pop(0)
    b_ans.append(vertex)
    for i in sorted(li[vertex]):
      if not b_visited[i-1]:
        b_visited[i-1] = True
        queue.append(i)


dfs(s)  
print(" ".join(map(str, d_ans)))
bfs(s)
print(" ".join(map(str, b_ans)))
  