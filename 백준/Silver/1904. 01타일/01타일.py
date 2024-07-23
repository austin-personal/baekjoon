def fib(n):
    for i in range(2, n+1):

        li[i] = (li[i-2] + li[i-1]) % 15746


x = int(input())

li = [1] * (x + 1)
fib(x)
print(li[x])