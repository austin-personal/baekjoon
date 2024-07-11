N = int(input())
top_list = list(map(int, input().split()))

def telCom():
    result = [0] * N
    stack = []

    for i in range(N):
        # 스택에 맨 마지막 오브젝트(인덱스)에 해당하는, "현재 스택에 담긴" 탑이 현재 탑 보다 작을시에 현재 있던 스택의 마지막을 뺀다. 
        while stack and top_list[stack[-1]] < top_list[i]:
            stack.pop()
        # 현재 탑에 대한 인덱스 결과 값에 스택의 마지막 인덱스에 +1을 한 수를 replace한다. 
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    return result

ans = telCom()
print(' '.join(map(str, ans)))


## 결국 스택이란 가장 큰 탑과 그 탑에 비치는 탑들이 담긴다. 

##############################################################################

## 첫번째 시도: 시간 복잡도가 O(n^2)이라 타임 아웃
N = int(input())
top_list = list(map(int, input().split()))


def telCom():
    result = []
    for i in range(N, 0, -1):
        if top_list[i-1] <= top_list[i - 2]:
            result.append(i-1)
        elif top_list[i-1] > top_list[i - 2]:
            change = 0
            for j in range(i-2, 0, -1):
                if top_list[i-1] <= top_list[j]:
                    result.append(j+1)
                    change+=1
                    continue
            if change==0:
                result.append(0)

    return result

t_list = telCom()
ans = []
for i in range(len(t_list),0,-1):
  ans.append(t_list[i-1])
print(ans)
  
  


