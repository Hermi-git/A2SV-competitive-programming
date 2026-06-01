class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[]for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
        answer =[]
        for i, node in enumerate(graph):
            if node == []:
                answer.append(i)
        return answer