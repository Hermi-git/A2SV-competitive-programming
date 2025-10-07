class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        memo ={}
        def dp(i, j):
            if i == m - 1:
                return triangle[i][j]
 
            if (i, j) not in memo:
                if 0 <= i < m and 0 <= j < len(triangle[i]):
                    memo[(i, j)] = triangle [i][j] + min(dp(i+1, j+1), dp(i+1, j))
            return memo[(i, j)]
        
        return dp(0, 0)
        