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