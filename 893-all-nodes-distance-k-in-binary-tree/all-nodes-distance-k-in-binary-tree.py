# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
        print(graph)
        answer = []
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                answer.append(node)
            if distance < k:
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, distance + 1))

        return answer


