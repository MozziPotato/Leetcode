# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        tree_layer_edges = dict()
        
        def BF_traverse(depth: int, prev_layer_edges: list):
            
            tree_layer_edges[depth] = prev_layer_edges
            
            next_layer_edges = []
            
            for prev_layer_edge in prev_layer_edges:
                left = prev_layer_edge[1].left
                right = prev_layer_edge[1].right
                if left:
                    next_layer_edges.append((prev_layer_edge[1],left))
                if right:
                    next_layer_edges.append((prev_layer_edge[1],right))
                    
            if not next_layer_edges:
                deepest_nodes = [edge[1] for edge in tree_layer_edges[depth]]
                return find_subtree_root(depth, deepest_nodes)
            else:    
                return BF_traverse(depth+1, next_layer_edges)
        
        def find_subtree_root(depth: int, subtree_nodes: list):
            
            # case: whole tree is subtree
            # case: single deepest node
            if len(subtree_nodes) == 1:
                return subtree_nodes[0]
            
            ancestors = set()
            
            for current_layer_edge in tree_layer_edges[depth]:
                if current_layer_edge[1] in subtree_nodes:
                    ancestors.add(current_layer_edge[0])
            
            if len(ancestors) != 1:
                return find_subtree_root(depth-1, ancestors)
            else:
                return ancestors.pop()
                
        return BF_traverse(0, [(None, root)])
    

            
            