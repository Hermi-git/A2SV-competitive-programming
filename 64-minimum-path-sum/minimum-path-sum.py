class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo ={}
        def dp(i, j):
            if i == (m-1) and j == (n-1):
                return grid[i][j]
            if i >= m or j >= n:
                return float("inf")
 
            if (i, j) not in memo:
                if 0 <= i < m and 0 <= j < n:
                    memo[(i, j)] = grid[i][j] + min(dp(i, j+1), dp(i+1, j))
            return memo[(i, j)]
        
        return dp(0, 0)
