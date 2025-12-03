# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q= deque([(root, None)])
        ans = 0
        while q:
            child, parent = q.popleft()

            if not child.left and not child.right:
                if parent and child == parent.left:
                    ans += child.val
            
            if child.left: q.append((child.left, child))
            if child.right: q.append((child.right, child))
        return ans