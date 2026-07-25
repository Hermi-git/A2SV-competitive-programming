class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        height = [[-1 for _ in range(n)]for _ in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    height[r][c] = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if inbound(nr, nc) and height[nr][nc] == -1:
                    queue.append((nr, nc))
                    height[nr][nc] = height[r][c] +1
        return height
        