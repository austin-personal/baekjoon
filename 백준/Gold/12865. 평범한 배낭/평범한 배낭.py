"""
import sys

def knapsack(N, M, items):
    # Initialize DP table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Iterate over each item
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        # Iterate over each capacity from 0 to M
        for j in range(1, M + 1):
            if weight <= j:
                # Calculate the maximum value by including or excluding the item
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight] + value)
            else:
                # If the item's weight is more than the current capacity, exclude the item
                dp[i][j] = dp[i - 1][j]
    
    # # Print the dp table for debugging
    # for row in dp:
    #     print(row)
    
    # The maximum value that can be achieved with given weight capacity M
    return dp[N][M]

# Read input
N, M = map(int, sys.stdin.readline().rstrip().split())
items = []
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().rstrip().split())))

# Calculate and print the result
result = knapsack(N, M, items)
print(result)

"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
#DP표는 0~K+1, 0~N+1로 구성하자 (N=1일 때, DP[i-1][j]가 존재해야 하므로)

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]:  #"현재최대무게j가 해당물건무게보다 큰 경우
        #표의 윗 셀의 값과 현재물건의V+이전물건의V값의 최댓값을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
        else:
        	#"현재최대무게j가 해당물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            dp[i][j] = dp[i-1][j]

print(dp[N][K])