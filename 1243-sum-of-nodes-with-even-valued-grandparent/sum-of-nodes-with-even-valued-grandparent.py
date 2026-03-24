# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        evensum = 0
        def dfs(node, parent, grandparent):
            nonlocal evensum
            if not node:
                return 0
            if grandparent:
                if grandparent.val % 2 == 0:
                    evensum += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
            return evensum
        return dfs(root, None, None)
                    
