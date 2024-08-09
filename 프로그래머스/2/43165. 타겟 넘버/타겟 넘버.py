
def dfs(index, current_sum, numbers, target):
  if index == len(numbers):
    if current_sum == target:
      return 1
    else:
      return 0
  return dfs(index + 1, current_sum + numbers[index], numbers, target) + dfs(
      index + 1, current_sum - numbers[index], numbers, target)


def solution(numbers, target):
  answer = dfs(0, 0, numbers, target)
  return answer
