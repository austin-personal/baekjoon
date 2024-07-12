""" 
Key take aways:
1. Use a dictionary to store the tree structure. (key: root, value: left, right child)
2. Implement a recursive function to traverse the tree in preorder, inorder, and postorder.
3. Use sys.stdin.readline() to read input efficiently.
4. Print the results with a space separator and no newline character at the end.

Time Complexity: O(n)
"""



import sys

# Take 인접노드 

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split() 
    # strip() removes tab, enter and space when it reads a line.
    tree[root] = [left, right]
  

# print 전위 중위 후위 
# 전위

def preorder(root):
  # When it is root,
  if root != '.':
    print(root, end='') #현재 루트(노드를 바로 출력), 끝에 빈공간없이 설정을 하여 연속적인 출력가능. 
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
  if root != '.':
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
  if root != '.':
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root,end ='')
  
# 함수 실행하기
preorder('A')
print()
inorder('A')
print()
postorder('A')
 