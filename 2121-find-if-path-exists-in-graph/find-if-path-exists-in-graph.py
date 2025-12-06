class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for node in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(start, end):
            if start == end:
                return True
            visited.add(start)
            for neigh in adj_list[start]:
                if neigh not in visited:
                    if dfs(neigh, end):
                        return True
            return False
        return dfs(source, destination)