class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
    
        def dijkstra(start):
            dist = {node: float('inf') for node in graph}
            cnt=-1
            dist[start] = 0
            
            heap = [(0, start)]
            while heap:
                current_distance, current_node = heapq.heappop(heap)
                for child, weight in graph[current_node]: 
                    distance = current_distance + weight
                    if distance < dist[child]:
                        dist[child] = distance
                        heapq.heappush(heap, (distance, child))
            for d in dist.values():
                if d<=distanceThreshold:
                    cnt+=1
            return cnt
            
        cnt_nodes=[0]*(n)
        for i in range(n):
            cnt_nodes[i]=dijkstra(i)
        ans=float("inf")
        result=None
        for i in range(n):
            if cnt_nodes[i]<=ans:
                ans=cnt_nodes[i]
                result=i
        return result
