# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs_depth(node):
            if not node:
                return 0
            return 1 + max(dfs_depth(node.left), dfs_depth(node.right))
        
        return dfs_depth(root)