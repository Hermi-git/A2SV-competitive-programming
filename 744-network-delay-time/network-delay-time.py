class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v , time in times:
            graph[u].append((v, time))
        
        min_time = [float('inf') for _ in range(n+1)]
        min_time[k] = 0

        heap = [(0, k)]
        while heap:
            curr_time, node = heapq.heappop(heap)
            for v, time in graph[node]:
                new_time = curr_time + time
                if new_time < min_time[v]:
                    min_time[v] = new_time
                    heapq.heappush(heap, (new_time, v))
    
        ans = max(min_time[1:])
        return ans if ans != float('inf') else -1

