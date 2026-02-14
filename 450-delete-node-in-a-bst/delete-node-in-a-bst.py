# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(node):
            while node.left:
                node = node.left
            return node
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val == key: 
            #if a node has not child at all or has left or right child 
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            #if node has two child nodes
            inorder_successor = findmin(root.right)
            root.val = inorder_successor.val
            root.right = self.deleteNode(root.right, inorder_successor.val)
        return root
