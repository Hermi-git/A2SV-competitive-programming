class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        q = deque()
        visited = set()
        
        for node in range(n):
            if degree[node] == 1:
                q.append(node)
                visited.add(node)
        layer = []
        while q:
            order = []

            for _ in range(len(q)):
                node = q.popleft()
                order.append(node)
                for neigh in graph[node]:
                    degree[neigh] -= 1
                    if neigh not in visited and degree[neigh] == 1:
                        q.append(neigh)
                        visited.add(neigh)
            layer.append(order)
        return layer[-1] if layer != [] else [0]