# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        parent[root] = None
        def dfs(node):
            if node:
                if node.left:
                    parent[node.left] = node
                    dfs(node.left)
                if node.right:
                    parent[node.right] = node
                    dfs(node.right)
        dfs(root)    
        nodes = []
        q = deque([(target, 0)])
        visited = set([(target)])
        while q:
            node, distance = q.popleft()
            if not node:
                continue
            if distance == k:
                nodes.append(node.val)
            if node.left and node.left not in visited: 
                q.append((node.left, distance +1))
                visited.add((node.left))
            if node.right and node.right not in visited: 
                q.append((node.right, distance +1))
                visited.add(node.right)
            if parent[node] and parent[node] not in visited: 
                q.append((parent[node], distance +1))
                visited.add(parent[node])
        return nodes

