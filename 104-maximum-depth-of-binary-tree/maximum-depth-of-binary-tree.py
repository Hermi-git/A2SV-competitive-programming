# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(curr):
            if not curr:
                return 0
            return 1 + max(max_depth(curr.left), max_depth(curr.right))
        return max_depth(root)