"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # LETS DO BFS
        if not node:
            return None

        search_stack = [node]
        old_to_new = {node: Node(node.val)}

        while search_stack:
            curr_node = search_stack.pop()
            
            for neighb in curr_node.neighbors:
                if neighb not in old_to_new:
                    old_to_new[neighb] = Node(neighb.val)
                    search_stack.append(neighb)
                neighb_clone = old_to_new[neighb]
                curr_clone = old_to_new[curr_node]
                curr_clone.neighbors.append(neighb_clone)
            
            
        return old_to_new[node]
        