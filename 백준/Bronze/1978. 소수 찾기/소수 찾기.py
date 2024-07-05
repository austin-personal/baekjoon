N=int(input())
nums = map(int, input().split())
p_num=0
for num in nums:
  if num>1:
    count=0
    for i in range(2,num):
      if num%i == 0:
        count+=1
    if count == 0:
      p_num+=1
print(p_num)