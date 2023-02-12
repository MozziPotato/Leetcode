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
            # original graph의 node 방문
            p = q.popleft()
            # cloned node를 return
            curr = adjacency[p.val]
            # original graph의 node의 이웃을 모두 방문
            for neighbor in p.neighbors:
                # 이웃을 방문한 적이 없다면 Hashing & enqueue
                if neighbor.val not in visited.keys():
                    visited[neighbor.val] = True
                    q.append(neighbor)
                # 이웃을 cloning한 적이 없다면 Hashing & Cloning
                if neighbor.val not in adjacency.keys():
                    adjacency[neighbor.val] = Node(neighbor.val)
                # cloned node의 이웃으로 original graph의 이웃을 저장
                curr.neighbors.append(adjacency[neighbor.val])
                
        return root