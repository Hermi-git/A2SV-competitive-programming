class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree =[0] * (n+1)
        graph = defaultdict(list)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for course in range(1, n+1):
            if indegree[course] == 0:
                q.append(course)

        finish_month = time[:]
        while q:
            course = q.popleft()
            for neigh in graph[course]:
                finish_month[neigh-1] =max(finish_month[neigh-1], finish_month[course-1]+ time[neigh-1])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
       
        return max(finish_month)               
