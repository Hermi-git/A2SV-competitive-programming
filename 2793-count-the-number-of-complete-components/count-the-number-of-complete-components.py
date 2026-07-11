class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[]for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        def dfs(node, connected):
            visit.add(node)
            connected.append(node)
            for neigh in graph[node]:
                if neigh not in visit:
                    dfs(neigh, connected)
        
        components =0
        for node in range(n):
            if node not in visit:
                connected = []
                dfs(node, connected)
                
                total_edges= 0
                for node in connected:
                    total_edges += len(graph[node])
                total_edges //= 2

                m = len(connected)
                if total_edges == m*(m-1)//2:
                    components += 1
        return components
        