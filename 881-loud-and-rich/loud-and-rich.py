class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
        q = deque()
        answer = [i for i in range(n)]
        for rich in range(n):
            if indegree[rich] == 0:
                q.append(rich)
        while q:
            richer = q.popleft()
            for poorer in graph[richer]:
                if quiet[answer[richer]] < quiet[answer[poorer]]:
                    answer[poorer] = answer[richer]
                indegree[poorer] -= 1
                if indegree[poorer] == 0:
                    q.append(poorer)
        return answer


