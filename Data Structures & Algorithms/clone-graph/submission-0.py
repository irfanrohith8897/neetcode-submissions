"""
# Definition for a Node.
class Node:
    def __init__(self, val  =  0, neighbors  =  None):
        self.val  =  val
        self.neighbors  =  neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root = Node(node.val)
        queue = deque([node])
        map = {}
        map[node] = root

        while queue:

            original_node = queue.popleft()
            current_node = map[original_node]

            for i in original_node.neighbors:
                if i not in map:
                    cloned_node = Node(i.val)
                    current_node.neighbors.append(cloned_node)
                    queue.append(i)
                    map[i] = cloned_node
                else:
                    current_node.neighbors.append(map[i])
        return root
                
        