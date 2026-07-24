class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        direction = [(0, 1), (1, 0), (-1,0), (0, -1)]
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        distance = [[-1 for _ in range(n)]for _ in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    distance[r][c] = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc
                    if inbound(nr, nc) and distance[nr][nc] == -1:
                        q.append((nr, nc))
                        distance[nr][nc] = distance[r][c] + 1
        return distance
            

                
                    