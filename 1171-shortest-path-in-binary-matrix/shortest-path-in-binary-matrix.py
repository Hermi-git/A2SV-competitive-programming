class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        q = deque([(0, 0, 1)])
        visited = set((0,0))

        while q:
            r, c, length = q.popleft()
            if grid[r][c]:
                continue
            if r == n-1 and c == n-1:
                return length
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if inbound(new_r, new_c) and (new_r, new_c) not in visited:
                    q.append((new_r, new_c, length+1))
                    visited.add((new_r, new_c))
        return -1
                