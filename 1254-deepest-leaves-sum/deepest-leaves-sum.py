# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return  1 + max(dfs(node.left), dfs(node.right))
        max_depth = dfs(root)
        q = deque([(root, 1)])
        answer = 0
        while q:
            node, depth= q.popleft()
            if not node:
                continue
            if not node.left and not node.right and depth == max_depth:
                answer += node.val
            if node.left: q.append((node.left, depth + 1))
            if node.right: q.append((node.right, depth + 1))
        return answer
        