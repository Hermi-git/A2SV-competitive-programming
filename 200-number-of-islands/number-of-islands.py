class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inbound(row, col):
            return 0<=row<n and 0<=col<m
        
        visited = [[False for _ in range(m)]for _ in range(n)]
        def dfs(row, col):
            visited[row][col] = True

            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                    dfs(new_row, new_col)
        island_count = 0
        for r in range(n):
            for c in range(m):
                if not visited[r][c] and grid[r][c] == "1":
                    dfs(r, c)
                    island_count += 1
        return island_count