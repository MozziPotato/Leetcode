# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(-float('inf'))
        self.change1, self.change2 = None, None
        
        self.get2nodes(root)
        
        self.change1.val, self.change2.val = self.change2.val, self.change1.val
        
    def get2nodes(self, root):
        if root:
            self.get2nodes(root.left)
            
            if self.prev.val > root.val:
                if not self.change1:
                    self.change1 = self.prev
                self.change2 = root
                
            self.prev = root
        
            self.get2nodes(root.right)
            
        # mistake는 무엇인가? BST의 property를 위배하는 것을 의미함.
        # 그럼 BST의 property는 무엇인가? root node를 기준으로 left child는 그 값이 작고, right child는 그 값이 커야 함.
        # 따라서 mistake를 식별할 수 있도록, 크기를 비교하는 로직이 필요.
        
        # mistake를 찾아냈다면, BST의 property를 유지하도록 조정해야 한다.
        # 만약 인접한 root와 child 관계에서 property가 위배되었다면, 단순히 두 노드의 위치를 바꾸면 되니까 간단하게 해결할 수 있다.
        
        # 문제는 두 node가 떨어져 있을 때이다. (example 2)
        # 단순히 인접한 node간의 비교로는 해결할 수가 없다.
        # 그렇다고 모든 ancestor의 값을 다 들고 있자니 memory 공간을 차지할 뿐만 아니라, -> O(1) space solution!
        # right ancestor인지 left ancestor인지 등에 대해 로직을 세우는 것이 복잡해진다.
        # 즉, 이렇게 풀면 안된다.
                
        # 이번 강의에서 preorder, inorder, postorder의 용례에 대해서 설명해주셨는데,
        # inorder의 경우 BST를 sorted list로 변경할 때에 사용할 수 있다.
        # 따라서 inorder를 사용해서 BST를 탐색한 후, 그 결과에서 sorted 되어 있지 않은 노드를 찾아내서 바꿔주면 쉽게 처리할 수 있을 것이다.
        # 문제는 constant memory space인 O(1) 안에 풀어야 한다는 것이다. 그렇다면 어떻게 해야할까?
        # order를 깨는 node를 발견할 때까지 inorder로 순회한 후,
        # 해당 node를 기억해둔 상태에서 inorder를 다시 탐색하여 최종 swap을 수행한다.
        
#         def inorder_find_breaker(node: Optional[TreeNode], last_node):
            
#             if node.left:
#                 last_node = inorder_find_breaker(node.left, last_node)
#                 if last_node.val > node.val:
#                     swap(last_node, node)
#                     return last_node
            
#             if node.right:
#                 last_node = inorder_find_breaker(node.right, node)
#                 if node.val > last_node.val:
#                     swap(last_node, node)
#                     return node
#                 else:
#                     return node.right
            
#             return node
        
#         start_node = TreeNode(-math.inf)
#         breaker_node = inorder_find_breaker(root, start_node)