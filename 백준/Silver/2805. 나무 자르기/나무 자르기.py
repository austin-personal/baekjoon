N, M = map(int, input().split())
tree = list(map(int, input().split()))

def cutting(m):
    start = 0
    end = max(tree)

    while start <= end:
        sum_branch = 0
        mid = (start + end) // 2
        for i in tree:
            if i > mid:
                sum_branch += i - mid

        if sum_branch >= m:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(cutting(M))
