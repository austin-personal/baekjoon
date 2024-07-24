import sys

E = list(map(str, sys.stdin.readline().rstrip().split("-")))

def evaluate_sum(part):
    return sum(map(int, part.split('+')))

result = evaluate_sum(E[0])
if len(E) ==1:
    print(result)
# 파트가 1개 이상일때
else:
    for part in E[1:]:
        # 파트 
        result -= evaluate_sum(part)

    print(result)