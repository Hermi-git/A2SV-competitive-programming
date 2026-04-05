# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = []
        def difference(node, ancestors):
            if not node:
                return
            for ancestor in ancestors:
                res.append(abs(ancestor - node.val))
            difference(node.left, ancestors + [node.val])
            difference(node.right, ancestors + [node.val])
        difference(root, [])
        return max(res)