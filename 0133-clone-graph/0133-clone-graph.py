"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return
        
        # original graph의 BFS를 위한 Hashing (방문 여부를 value로)
        q = deque([node])
        visited = dict()
        visited[node.val] = True
        
        # clone graph를 위한 Hashing (Node class를 value로)
        root = Node(node.val)
        adjacency = dict()
        adjacency[root.val] = root
        
        while q:
            p = q.popleft()
            curr = adjacency[p.val]
            for neighbor in p.neighbors:
                if neighbor.val not in visited.keys():
                    visited[neighbor.val] = True
                    q.append(neighbor)
                if neighbor.val not in adjacency.keys():
                    adjacency[neighbor.val] = Node(neighbor.val)
                curr.neighbors.append(adjacency[neighbor.val])
                
        return root