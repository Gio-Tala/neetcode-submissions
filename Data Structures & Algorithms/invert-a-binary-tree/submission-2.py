# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursively invert left and right subparts
        def switch_sides(switch_root):
            if not switch_root:
                return
            switch_root.left, switch_root.right = switch_root.right, switch_root.left
            switch_sides(switch_root.left)
            switch_sides(switch_root.right)
        switch_sides(root)
        return root
        