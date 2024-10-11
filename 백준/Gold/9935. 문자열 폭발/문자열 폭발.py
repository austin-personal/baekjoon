# mirkovC4nizCC44
# C4
# mirkovniz

# 12ab112ab2ab
# 12ab
# FRULA

# 폭탄 문장이 완성될때 삭제.
  # 스택 사용해서 없엘수 있을때, 삭제남는것은 그대로, 
# 없을때는 FRULA

def remove_bomb(sentence, bomb):
  stack = []
  bomb_length = len(bomb)

  for char in sentence:
    stack.append(char)
    if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == bomb:
      del stack[-bomb_length:]

  result = ''.join(stack)
  return result if result else "FRULA"


sentence = input().strip()
bomb = input().strip()


result = remove_bomb(sentence, bomb)
print(result)