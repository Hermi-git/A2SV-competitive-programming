class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v , time in times:
            graph[u].append((v, time))
        
        times = {}
        heap = [(0, k)]  

        while heap:
            time_k_to_node, node = heapq.heappop(heap)
            if node in times:
                continue
            times[node] = time_k_to_node
            for neigh, neigh_time in graph[node]:
                if neigh not in times:
                    heapq.heappush(heap, (time_k_to_node + neigh_time, neigh))
        return max(times.values()) if len(times) == n else -1
        
       