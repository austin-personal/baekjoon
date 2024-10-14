# 단어의 계수(N)와 총 가르칠수 있는 레터들의 수(K)가 입력된다.
# 모든 단어는 anta로 시작, tica로 끝난다. a,n,t,i,c의 레터들은 무조건 사용이 된다.
# 주어진 단어들중에 a,n,t,i,c를 포함해서,
# 총가르칠수 있는 레터에 수를 넘지 않는 단어들의 수를 반환 해라.

# 1. 총 가르칠수 있는 수가 5개 미만이라면 반환은 무조건 0이다.
# 5개 이상일때, K-5개의 추가적인 레터들을 학습할수 있다.

from itertools import combinations


def count_readable_words(words, learned):
  count = 0
  for word in words:
    can_read = True
    for char in word:
      if not learned[ord(char) - ord('a')]:
        can_read = False
        break
    if can_read:
      count += 1
  return count


def solve():
  n, k = map(int, input().split())

  # 가르칠 수 있는 글자가 5 미만이면 어떤 단어도 읽을 수 없다.
  if k < 5:
    print(0)
    return

  # 기본적으로 알아야 하는 글자 (antic)
  essential_chars = set(['a', 'n', 't', 'i', 'c'])
  learned = [False] * 26  # 알파벳 26개의 배운 여부를 저장하는 리스트
  for char in essential_chars:
    learned[ord(char) - ord('a')] = True

  words = []
  for _ in range(n):
    word = input().strip()
    # anta와 tica를 제외한 단어 부분만 추출
    words.append(set(word[4:-4]))

  # 가능한 모든 글자를 추출 (중복 제거)
  possible_chars = set()
  for word in words:
    possible_chars.update(word)

  # 이미 배운 글자는 제외
  possible_chars = list(possible_chars - essential_chars)

  # 배울 수 있는 추가 글자의 수
  additional_learn = k - 5

  # 배울 글자가 없거나 배울 수 있는 글자 수보다 가능한 글자가 적을 경우
  if additional_learn <= 0 or len(possible_chars) <= 0:
    # 이미 배운 글자들만으로 읽을 수 있는 단어 계산
    print(count_readable_words(words, learned))
    return

  max_count = 0

  # possible_chars에서 추가로 배울 글자들 중 k-5개의 글자를 선택하는 모든 조합을 계산
  for comb in combinations(possible_chars,
                           min(additional_learn, len(possible_chars))):
    # 현재 선택한 글자를 배운 것으로 표시
    for char in comb:
      learned[ord(char) - ord('a')] = True

    # 이 조합으로 읽을 수 있는 단어 개수 계산
    count = count_readable_words(words, learned)
    max_count = max(max_count, count)

    # 선택한 글자를 다시 안 배운 것으로 표시
    for char in comb:
      learned[ord(char) - ord('a')] = False

  print(max_count)


# 실행
solve()
