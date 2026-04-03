# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = []
        def bst_inorder(node):
            if node:
                bst_inorder(node.left)
                answer.append(node.val)
                bst_inorder(node.right)
        bst_inorder(root)
        correct_bst = sorted(answer)
        return answer == correct_bst and len(answer) == len(set(answer))
        
        