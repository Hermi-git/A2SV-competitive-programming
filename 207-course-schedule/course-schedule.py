class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses 
        graph = [[] for _ in range(n)]
        for u, v in prerequisites:
            graph[v].append(u)

        white, gray, black = 0, 1, 2
        color = [white for _ in range(n)]
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return 
            color[node] = gray
            for neigh in graph[node]:
                if color[neigh] == white:
                    dfs(neigh)
                elif color[neigh] == gray:
                    no_cycle = False
            
            color[node] = black
            return no_cycle
        ans =True  
        for course in range(n):
            if color[course] == white:
                ans = ans and dfs(course)  
        return ans  


