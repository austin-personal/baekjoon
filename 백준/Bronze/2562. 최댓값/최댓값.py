numList=[]
for _ in range(9):
  a=int(input())
  numList.append(a)

max=max(numList)
iMax=numList.index(max)
print(max)
print(iMax+1)
