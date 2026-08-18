class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reverse_graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            reverse_graph[course].append(pre)
            indegree[pre] += 1
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        isReachable = [set() for _ in range(numCourses)]
        while q:
            course = q.popleft()
            for c in reverse_graph[course]:
                isReachable[c].update(isReachable[course])
                isReachable[c].add(course)
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        answer = [False] * len(queries)
        for i, (p, c)in enumerate(queries):
            if c in isReachable[p]:
                answer[i] =True
        return answer



        

            

                    

