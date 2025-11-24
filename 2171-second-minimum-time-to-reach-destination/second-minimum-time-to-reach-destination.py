class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([1])
        curr_time = 0
        res = -1
        visited = defaultdict(list)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return curr_time
                    res = curr_time
                for neigh in graph[node]:
                    neigh_times = visited[neigh]
                    if len(neigh_times) == 0 or len(neigh_times) == 1 and neigh_times[0] != curr_time:
                        q.append(neigh)
                        neigh_times.append(curr_time)
            if (curr_time // change) %2 == 1:
                curr_time += change - (curr_time % change)
            curr_time += time
        
        


                
