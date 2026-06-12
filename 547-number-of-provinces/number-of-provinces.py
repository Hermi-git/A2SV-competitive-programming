class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = [[] for _ in range(n)]
        for r in range(n):
            for c in range(r+1,n):
                if isConnected[r][c] == 1:
                    adj_list[r].append(c)
                    adj_list[c].append(r)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in adj_list[node]:
                if neigh not in visited:
                    dfs(neigh)
        provinces = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                provinces += 1
        return provinces
