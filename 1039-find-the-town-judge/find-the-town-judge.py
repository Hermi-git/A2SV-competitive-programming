class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0 for _ in range(n+1)]
        outdegree = [0 for _ in range(n+1)]
        for u, v in trust:
            outdegree[u] += 1
            indegree[v] += 1
        for node in range(1, n+1):
            if indegree[node] == n-1 and outdegree[node] == 0:
                return node
        return -1