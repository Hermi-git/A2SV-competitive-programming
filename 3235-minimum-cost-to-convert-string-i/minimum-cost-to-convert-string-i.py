class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf' )]* 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        
        for i in range(len(cost)):
            s = ord(original[i]) - 97
            t = ord(changed[i]) - 97
            c = cost[i]
            dist[s][t] = min(dist[s][t], c)
       
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]


        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            i = ord(s) - 97
            j = ord(t) - 97
            if dist[i][j] == float('inf'):
                return -1
            ans += dist[i][j]
        return ans 

