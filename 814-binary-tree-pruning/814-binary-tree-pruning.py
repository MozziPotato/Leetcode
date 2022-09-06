# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def check(root):
                
            l_subtree, l_contain = check(root.left) if root.left else (None, False)
            r_subtree, r_contain = check(root.right) if root.right else (None, False)

            if l_subtree:
                if not l_contain:
                    if l_subtree.val == 1:
                        l_contain = True
                    else:
                        l_contain = False
                        root.left = None

            if r_subtree:
                if not r_contain:
                    if r_subtree.val == 1:
                        r_contain = True
                    else:
                        r_contain = False
                        root.right = None
                
            return root, l_contain or r_contain
        
        root, contain = check(root)
        
        if root.val == 0 and not (root.left or root.right):
            return None
        
        return root