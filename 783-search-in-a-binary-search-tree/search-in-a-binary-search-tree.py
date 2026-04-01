# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if not node:
                return None
            if val == node.val:
                return node
            if val < node.val:
                return search(node.left) 
            if val > node.val:
                return search(node.right)
        return search(root)
            