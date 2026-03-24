# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countFrom(node, remaining):
            path = 0
            if not node:
                return 0 
            remaining -= node.val 
            if remaining == 0:
                path += 1  
            return path + countFrom(node.left, remaining) + countFrom(node.right, remaining)
            
        totalPath = 0
        def traverse(node):
            nonlocal totalPath
            if not node:
                return 
            
            totalPath += countFrom(node, targetSum)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return totalPath