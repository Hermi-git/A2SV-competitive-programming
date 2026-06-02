class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[]for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(start, end):
            if start == end:
                return True
            visited.add(start)
            for neigh in graph[start]:
                if neigh not in visited:
                    if dfs(neigh, end):
                        return True
            return False
        
        return dfs(source, destination)
