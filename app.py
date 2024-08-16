N = int(input())
classes = [0 for _ in range(N)]
result = 0

for i in range(N):
    classes[i] = list(map(int, input().split()))

classes.sort(key=lambda x: (x[1]))
recent_end = float("inf")
ends = []

for cls in classes:
    if cls[1] >= recent_end:
        ends.append(cls[2])
        ends.remove(recent_end)
        recent_end = min(ends)

    if cls[1] < recent_end:
        ends.append(cls[2])
        print(ends)
        result += 1

        if cls[2] < recent_end:
            recent_end = cls[2]

print(result)