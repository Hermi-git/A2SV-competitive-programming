# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxdiff = 0
        def diff(node, cur_min, cur_max):
            nonlocal maxdiff
            if not node:
                return 0
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            maxdiff = max(maxdiff, cur_max - cur_min)

            left = diff(node.left, cur_min, cur_max)
            right = diff(node.right, cur_min, cur_max)

            return maxdiff
        return diff(root, root.val, root.val) if root else diff(root, 0, 0)
            
         
            
            
