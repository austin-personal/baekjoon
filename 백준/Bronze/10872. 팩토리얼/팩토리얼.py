def fact(n):
  if n <= 1:
    return 1
  else:
    return n*fact(n-1)


a = int(input())

print(fact(a))


#Key points 
  # n = 0으로 최초에 인풋한경우까지 생각해서 n<=1
  # return 5 *4 *3 *2 *1를 상상해라
  # 함수가 끝나지 않는이상 계산을 하지 않고 계속 식을 쓰는 것이다. 
  # 함수가 끝나야 그동안 쓴 식을 계산한다. 
  