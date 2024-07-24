
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = []

for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))
coins.sort(reverse=True)
ans=0

for coin in coins:
    rest = K % coin

    if rest != K:
        count = K // coin
        ans += count
        K = rest

print(ans)