class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] +=1
        q = deque()
        ancestors = [set() for _ in range(n)]
        for node in range(n):
            if indegree[node] == 0:
                q.append((node))
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                ancestors[neigh].update(ancestors[node])
                ancestors[neigh].add(node)
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
                
        return [sorted(s) for s in ancestors]
