import heapq as hq
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
heap = []

for i in range(1, n + 1):
    new = int(data[i])
    if new != 0:
        # Push the negative value to maintain a max-heap property using heapq
        hq.heappush(heap, (-new, new))
    else:
        if heap:
            # Pop the largest value
            print(hq.heappop(heap)[1])
        else:
            print(0)
