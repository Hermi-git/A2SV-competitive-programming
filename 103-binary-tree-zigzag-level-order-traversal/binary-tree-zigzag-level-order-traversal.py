# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        level = 0
        ans = []
        cur_level_elem = []

        while queue:
            node, nodelevel = queue.popleft()

            if not node:
                continue
            if level != nodelevel:
                if level % 2 == 0:
                    ans.append(cur_level_elem[:])
                else:
                    ans.append(cur_level_elem[::-1])
                level += 1
                cur_level_elem = []
            cur_level_elem.append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        if cur_level_elem:
            if level != nodelevel:
                if level % 2 == 0:
                    ans.append(cur_level_elem[:])
                else:
                    ans.append(cur_level_elem[::-1])
        return ans 
        