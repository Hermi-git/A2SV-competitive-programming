class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
    
        def dijkstra(start_node):
            distances = {node: float('inf') for node in graph}
            count=-1
            distances[start_node] = 0
            processed = set()

            heap = [(0, start_node)]
            while heap:
                current_distance, current_node = heapq.heappop(heap)
                if current_node in processed:
                    continue
                processed.add(current_node)
                for child, weight in graph[current_node]: 
                    distance = current_distance + weight
                    if distance < distances[child]:
                        distances[child] = distance
                        heapq.heappush(heap, (distance, child))
            for d in distances.values():
                if d<=distanceThreshold:
                    count+=1
            return count
            
        count_nodes=[0]*(n)
        for i in range(n):
            count_nodes[i]=dijkstra(i)
        ans=float("inf")
        res=None
        for i in range(n):
            if count_nodes[i]<=ans:
                ans=count_nodes[i]
                res=i
        return res
