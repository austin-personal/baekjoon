# 1초 = 1억
# 예를 들어 N의 최대값이 10만이라고 문제에서 주어진다면

# 1. O(N) 의 시간복잡도일 경우에 값이 10만 정도이니, 1/1000초 정도가 걸릴 것이라고 예상할 수 있다.

# 2. O(N^2)의 시간복잡도의 경우에 값은 100억이므로, 100초 정도가 걸릴 것이라고 예상할 수 있다.

# 제한 시간은 1초, N의 크기는 최대 100이니까, 러프하게 100^3해도, 1억이 넘지 않음으로 for룹을 3중으로 사용해여, 모든 경우에 수를 찾아보자.


def blackJack(target, numList):
  tempNum = -1
  for firstInd in range(len(numList)):
    for secondInd in range(firstInd + 1, len(numList)):
      for thirdInd in range(secondInd + 1, len(numList)):
        sum = numList[firstInd] + numList[secondInd] + numList[thirdInd]
        if sum > target:
          continue
        if sum > tempNum:
          tempNum = sum
  print(tempNum)


N,target =map(int, input().split())
numList = list(map(int, input().split()))

blackJack(target, numList)
