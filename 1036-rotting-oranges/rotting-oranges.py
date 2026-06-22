class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 1
        rotten = 2
        fresh_oranges = 0
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def inbound(r, c):
            return 0<=r<n and 0<=c<m
        minutes = 0
        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == rotten:
                    q.append((r, c))
                elif grid[r][c] == fresh:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        while q:
            rotted_this_round = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if inbound(nr, nc) and grid[nr][nc] == fresh:
                        grid[nr][nc] = rotten
                        fresh_oranges -= 1
                        rotted_this_round = True
                        q.append((nr, nc))
            if rotted_this_round:
                minutes += 1
        return minutes if fresh_oranges == 0 else -1