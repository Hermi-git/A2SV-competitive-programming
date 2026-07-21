class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        q = deque([(0,0)])
        visited = set([(0, 0)])
        nodes = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == n-1 and col == n-1:
                    return nodes
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc 
                    if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            nodes += 1
        return -1
    

