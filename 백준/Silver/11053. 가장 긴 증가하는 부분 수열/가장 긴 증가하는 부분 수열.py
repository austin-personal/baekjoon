import sys

N = int(sys.stdin.readline().rstrip())

line = list(map(int, sys.stdin.readline().rstrip().split()))

uniq = list(set(line))
uniq.sort()

dp = [[0] * (len(line) + 1) for _ in range(len(uniq) + 1)]

for i in range(1, len(uniq)+1):
    for j in range(1, len(line)+1):

        if uniq[i-1] == line[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(uniq)][len(line)])
