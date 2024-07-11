num=temp=int(input())
count=0
while 1:
  ten=num//10
  one=num%10
  count +=1
  total=ten+one
  num=int(str(num%10)+str(total%10))
  if num == temp:
    break
print(count)
