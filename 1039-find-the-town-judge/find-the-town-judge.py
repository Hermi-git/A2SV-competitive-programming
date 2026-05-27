class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return n
        t_set = set([trust[i][0] for i in range(len(trust))])
        relation = defaultdict(list)
        for u, v in trust:
            relation[v].append(u)
        for node in relation:
            if len(relation[node]) == n-1 and node not in t_set:
                return node
        return -1
            
