class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, 'red'))
        for a, b in blueEdges:
            graph[a].append((b, 'blue'))
        
        answer = [-1] * n
        answer[0] =0
        visited = set([(0, 'red'), (0, 'blue')])
        q = deque([(0, 'red', 0), (0, 'blue', 0)])
        while q:
            node, edge, dist= q.popleft()
            for neigh, color in graph[node]:
                if (neigh, color) not in visited and color != edge:
                    visited.add((neigh, color))
                    q.append((neigh, color, dist +1))
                    if answer[neigh] == -1:
                        answer[neigh] = dist+1
        return answer
      
