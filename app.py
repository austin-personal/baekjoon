import sys

first_word = list(sys.stdin.readline().rstrip())
second_word = list(sys.stdin.readline().rstrip())


print(first_word, second_word)

dp = []

for i in first_word:
    for j in second_word:
        if first_word[i] == second_word[j]:
