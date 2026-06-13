class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            u = equations[i][0]
            v = equations[i][1]
            w = values[i]
            graph[u].append((v, w))
            graph[v].append((u, 1/w))
        def dfs( src, dst, visited):
            if src not in graph:
                return -1
            if src == dst:
                return 1
            visited.add(src)
            for neigh, weigh in graph[src]:
                if neigh not in visited:
                    result = dfs(neigh, dst, visited)
                    if result != -1:
                        return weigh * result
                       
            return -1
        
        answer = []
        for s,d in queries:
            val = dfs(s, d, set())
            answer.append(val)
        return answer 
