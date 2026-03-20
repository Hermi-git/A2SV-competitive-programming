# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        path = []
        def dfs(node, remaining):
            nonlocal path 
            if not node:
                return 
            remaining -= node.val 
            path.append(node.val)
            if not node.left and not node.right:
                if remaining == 0:
                    answer.append(path[:])    
            dfs(node.left, remaining)
            dfs(node.right, remaining)
            path.pop() 
        
        dfs(root, targetSum)
        return answer