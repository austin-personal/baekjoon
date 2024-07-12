
# ### First try which is incorrect
#         - 전위 값을 받아서
#             - 클래스로 정의
#         - 이진 트리를 만들고
#         - 후위로 변환


import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

preorder = []
while True:
    try:
      preorder.append(int(input()))
    except:
        break

# Object 설정
class TreeNode:
  def __init__(self, key):
      self.val = key
      self.left = None
      self.right = None

# Root는 이미 있는 값, 즉 페런트 노드. Key는 새로 들어온 값, 즉 chile node
def insert_node(root, key):
  # if there is not root, it means the key is the root
  if root is None:
      return TreeNode(key)
  # if there is root,
  else:
      # if root is lower than the new value which is key, set root at right
      if root.val < key:
          root.right = insert_node(root.right, key)
      # if root is higher than the new value which is key, set root at left
      else:
          root.left = insert_node(root.left, key)
  #???? Why return root is needed?
  return root

# 전위 값을 바탕으로 insert_node를 사용하여 BST 구조를 만든다. 
def construct_bst(preorder):
  # 예외 처리
  if not preorder:
      return None
  # 가장 높은 root는 전위 처리 리스트에서 가장 첫번째 숫자. 
  root = TreeNode(preorder[0])
  # 가장 높은거 다음 수 부터 그 다음 수의 크기에 따라 오른쪽에 넣을지, 왼쪽에 넣을지 확인 후 넣기
  for key in preorder[1:]:
      insert_node(root, key)
  return root

# 전위 리스트를 BST로 만든 후, 후위로 만들기. 
def postorder_traversal(node, result):
  if node:
      postorder_traversal(node.left, result)
      postorder_traversal(node.right, result)
      result.append(node.val)

# 앞에서의 모든 함수들을 실행시키는 함수
def find_postorder_from_preorder(preorder):
  # 전위를 이진 트리로 만드는 함수 콜
  root = construct_bst(preorder)
  result = []
  # 이진 트리를 후위로 출력하는 함수
  postorder_traversal(root, result)
  return result


# 후위 순회 결과 계산
postorder = find_postorder_from_preorder(preorder)
for i in postorder:
  print(i)

""" Second Try Below------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# Get 전위 숫자들
pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
# 후위 수열로 배출
def post(start, end):
    # 시작 인덱스가 끝 인덱스보다 커지면 끝
    if start > end:
        return
    # 미드 인덱스 초기화 for when any number in sub tree is not greater than parents node
    mid = end + 1
    # 무조건 부모노드인 start 값을 제외한 나머지 숫자들 Fol loop
    for i in range(start + 1, end + 1):
        # 첫 값과 i를 비교, 크면 새로운 미드 추가, 미드 추가는 새로운 브랜치 
        if pre[i] > pre[start]:
            mid = i
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리
    print(pre[start]) #루트 노드

post(0, len(pre) - 1)