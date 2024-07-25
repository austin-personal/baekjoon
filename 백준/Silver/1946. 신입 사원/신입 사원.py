import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    applicants = []
    for j in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().rsplit())
        applicants.append([a, b])
    applicants.sort(key = lambda x: (x[0], x[1]))
    selected = []
    first = applicants[0]
    selected.append(first)
    for j in range(1, len(applicants)):

        if selected[-1][1] > applicants[j][1] or first[0] > applicants[j][0]:
            selected.append(applicants[j])
            
    print(len(selected))




