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


# 소수의 특성상 어느 숫자의 num**0.5 만 체크해봐도 그 숫자가 소수인지 알수 있다. 