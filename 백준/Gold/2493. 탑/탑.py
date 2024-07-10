N = int(input())
top_list = list(map(int, input().split()))

def telCom():
    result = [0] * N
    stack = []

    for i in range(N):
        while stack and top_list[stack[-1]] < top_list[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    return result

ans = telCom()
print(' '.join(map(str, ans)))
