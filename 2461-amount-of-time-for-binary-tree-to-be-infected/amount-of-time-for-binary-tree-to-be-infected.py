# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def build_graph(node):
            if not node:
                return None
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)
        build_graph(root)
        
        queue = deque([start])
        visited = set([start])
        time = -1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            time += 1
        return time
                    

