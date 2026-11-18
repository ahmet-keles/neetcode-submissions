"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new_nodes = {}
        new_nodes[node.val] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val not in new_nodes:
                    new_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                new_nodes[cur.val].neighbors.append(new_nodes[neighbor.val])
        return new_nodes[node.val]        



