class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        black, brown, white = -1, 1, 0
        color = [black] * len(graph)
        visited = set()
        def dfs(node):
            for neigh in graph[node]:
                if neigh in visited:
                    if color[node] == color[neigh]:
                        return False
                else:
                    if color[neigh] == black:
                        if color[node] == white:
                            color[neigh] = brown
                        else:
                            color[neigh] = white
                    else:
                        color[neigh] = white
                    visited.add(neigh)
                    if not dfs(neigh):
                        return False 
            return True
        

        for node in range(len(graph)):
            if color[node] == black and node not in visited:
                color[node] = white
                if not dfs(node):
                    return False
        return True

