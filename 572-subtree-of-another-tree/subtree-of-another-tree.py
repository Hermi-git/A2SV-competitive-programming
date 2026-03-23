# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(s, t):
            if not s and not t:
                return True
            if not s and t is not None:
                return False
            if s is not None and not t:
                return False
            if s.val != t.val:
                return False
            return isIdentical(s.left,t.left) and isIdentical(s.right,t.right)
        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if isIdentical(node, subRoot):
                    return True
            
            return dfs(node.left) or dfs(node.right)
        return dfs(root)            

       

            
            
