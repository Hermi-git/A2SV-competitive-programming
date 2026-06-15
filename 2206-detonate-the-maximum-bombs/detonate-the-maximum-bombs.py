class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return ((x2 - x1) * (x2 - x1))  + ((y2 - y1 ) * (y2 - y1 ))
        nodes = len(bombs)
        graph = [[] for _ in range(nodes)]
        for i in range(nodes):
            for j in range(i+1, nodes):
                dist = distance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1])
                if dist <= (bombs[i][2]) * (bombs[i][2]):
                    graph[i].append(j)
                if  dist <= (bombs[j][2]) * (bombs[j][2]):
                    graph[j].append(i)
        
        def dfs(node, visited):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh, visited)
            return len(visited)
        
        max_bomb = 0
        for node in range(nodes):
            val = dfs(node, set())
            max_bomb = max(max_bomb, val)
        return max_bomb 