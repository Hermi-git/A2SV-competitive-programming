class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        q = deque()
        distance = [[-1 for _ in range(n)]for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    distance[r][c] = 0
        if not q or len(q) == n * n:
            return -1
        max_dist = float('-inf')
        while q:
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and distance[nr][nc] == -1:
                    q.append((nr, nc))
                    distance[nr][nc] = distance[r][c] + 1
                    max_dist = max(max_dist, distance[nr][nc])
        return max_dist if max_dist != float('-inf') else -1


