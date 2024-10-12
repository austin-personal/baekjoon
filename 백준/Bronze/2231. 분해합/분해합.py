def find_smallest_constructor(N):
  for i in range(1, N):
      if i + sum(int(digit) for digit in str(i)) == N:
          return i
  return 0


N = int(input())

result = find_smallest_constructor(N)

print(result)