import sys

N = int(sys.stdin.readline().rstrip())

meetings = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    meetings.append([a, b])

meetings.sort(key=lambda x: (x[1],x[0]))

meeting_list = []
for i in range(1, len(meetings)+1):
    if i == 1:
        meeting_list.append(meetings[0])
    elif meetings[i-1][0] >= meeting_list[-1][1]:
        meeting_list.append(meetings[i-1])


print(len(meeting_list))