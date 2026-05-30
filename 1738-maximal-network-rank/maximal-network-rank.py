class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        rank = 0
        for i in range(n):
            for j in range(i+1,n):
                if j in graph[i] or i in graph[j]:
                    rank = max(rank, len(graph[i])+len(graph[j])-1)
                else:
                    rank = max(rank, len(graph[i])+len(graph[j]))
        return rank
