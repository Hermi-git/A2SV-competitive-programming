class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def inbound(row, col):
            return 0<= row < n and 0<=col< m
        
        visited = [[False for _ in range(m)]for _ in range(n)]
        perimeter=0
        def dfs(row, col):
            nonlocal perimeter
            visited[row][col] = True

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter +=1

                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]:
                    dfs(new_row, new_col)
        for r in range(n):
            for c in range(m):
                if not visited[r][c]:
                    if grid[r][c] == 1:
                        dfs(r, c)
        return perimeter