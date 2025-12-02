# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, root.val)])

        while q:
            node, summ = q.popleft()
            if not node.left and not node.right:
                if summ == targetSum:
                    return True
            
            if node.left: q.append((node.left, summ + node.left.val))
            if node.right: q.append((node.right, summ + node.right.val))
        return False