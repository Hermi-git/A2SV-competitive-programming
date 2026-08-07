class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        revese_graph = [[] for _ in range(n)]
        out_degree = [0] * n
        for node in range(n):
            for neigh in graph[node]:
                revese_graph[neigh].append(node)
                out_degree[node] += 1
        
        q = deque()
        for node in range(n):
            if out_degree[node] == 0:
                q.append(node)
        safe_nodes = []
        while q:
            node= q.popleft()
            safe_nodes.append(node)
            for neigh in revese_graph[node]:
                out_degree[neigh] -= 1
                if out_degree[neigh] == 0:
                    q.append(neigh)
        
        return sorted(safe_nodes)





        