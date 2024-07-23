# import sys

# first_word = list(sys.stdin.readline().rstrip())
# second_word = list(sys.stdin.readline().rstrip())

# dp = []

# for i in range(len(first_word)):
#     dp.append([])
#     for j in range(len(second_word)):
#         dp[i].append(0)

#         # 첫 값일때
#         if i == j == 0:
#             # 첫 값이고 같을때
#             if first_word[i] == second_word[j]:
#                 dp[i][j] = 1
   
#             # 첫 값이고 다를때
#             else:
#                 dp[i][j] = 0
    
#         elif first_word[i] == second_word[j] and i == 0:
#             dp[i][j] = dp[i-1][j]+1
  
#         # 첫줄이 아니고, 같을 떼
#         elif first_word[i] == second_word[j]:
#             dp[i][j] = dp[i-1][j]+1

#         # 다를때
#         else:
#             # 다르고, 첫줄일때
#             if first_word[i] != second_word[j] and i == 0 :
#                 dp[i][j] = dp[i][j-1]
           
#             # 다르고 , 첫줄이 아닐때
#             else:
#                 if dp[i-1][j]> dp[i][j-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i][j-1]

# ans = dp[len(first_word)-1][len(second_word)-1]
# print(ans)