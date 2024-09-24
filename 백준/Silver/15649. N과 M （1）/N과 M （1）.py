N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)] # 1 부터 N 까지
path = [] 
visited = [False for _ in range(N+1)] 

def series(depth):
    if depth == M: 
        print(' '.join(map(str, path))) 
        return

    for i in num_list:
        if not visited[i]: 
            visited[i] = True  
            path.append(i)  
            series(depth + 1)  
            path.pop()  
            visited[i] = False  

series(0)