# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def bst(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            if p.val < node.val and q.val < node.val:
                return bst(node.left)
            if p.val > node.val and q.val > node.val:
                return bst(node.right)
            if p.val < node.val and q.val > node.val or p.val > node.val and q.val < node.val:
                return node
            
        return bst(root)