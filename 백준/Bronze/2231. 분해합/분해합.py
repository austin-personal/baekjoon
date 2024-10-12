def find_smallest_constructor(N):
  for i in range(1, N):
    if i + sum(int(digit) for digit in str(i)) == N:
      return i
  return 0


N = int(input())

result = find_smallest_constructor(N)

print(result)

# def find_original_number(n):
#   digits = [int(digit) for digit in str(n)]
#   nlen = len(digits)

#   # 각 자릿수의 최대 가능한 합 계산
#   max_sum = 9 * nlen

#   # 가능한 모든 조합 확인
#   for i in range(n - max_sum, n):
#       sum_digits = sum(int(digit) for digit in str(i))
#       if i + sum_digits == n:
#           return i

#   return None  # 해당하는 숫자를 찾지 못한 경우

# # 사용자 입력 받기
# n = int(input("숫자를 입력하세요: "))

# # 원래 숫자 찾기
# result = find_original_number(n)

# if result is not None:
#   print(f"입력한 숫자: {n}")
#   print(f"원래 숫자: {result}")
#   print(f"검증: {result} + {'+'.join(str(digit) for digit in str(result))} = {n}")
# else:
#   print("해당하는 원래 숫자를 찾을 수 없습니다.")