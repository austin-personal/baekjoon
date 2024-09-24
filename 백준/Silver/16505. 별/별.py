def Rec(i, x, y, count, arr):
    if i == 0:
        arr[x][y] = True
    else:
        count //= 2
        
        Rec(i-1, x, y, count, arr)
        Rec(i-1, x+count, y, count, arr)
        Rec(i-1, x, y+count, count, arr)


N = int(input()) #인풋받기

count = 2**N #인풋의 제곱의 수 = 시작 줄에 별 갯수(width), 총높이(heigh)

arr = [[False for _ in range(count)] for _ in range(count)] # 총높이, 총 넓이 만큼 리스트 만들기

Rec(N, 0, 0, count, arr) # 만든 arr에 별 넣기

for i in range(count):
    for j in range(count - i):
        if arr[i][j]:
            print("*", end="")
        else:
            print (" ", end="")
    print("")
