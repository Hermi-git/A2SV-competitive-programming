class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        out_graph = [[] for _ in range(len(graph))]
        out_degree = [0] * len(graph)
        for node in range(len(graph)):
            for neigh in graph[node]:
                out_graph[neigh].append(node)
                out_degree[node] += 1
        
        q = deque()
        for node in range(len(graph)):
            if out_degree[node] == 0:
                q.append(node)
        safe = []
        while q:
            node= q.popleft()
            safe.append(node)
            for neigh in out_graph[node]:
                out_degree[neigh] -= 1
                if out_degree[neigh] == 0:
                    q.append(neigh)
        sorted_safe = sorted(safe)
        return sorted_safe





        