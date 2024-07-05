N=int(input())
nums = map(int, input().split())
ss=0
for num in nums:
  if num>1:
    error=0
    for i in range(2,num):
      if num%i == 0:
        error+=1
    if error == 0:
      ss+=1
print(ss)