class Solution:
    def numSquares(self, n: int) -> int:
        def count_squares(x):
            perfect = []
            i = 1
            while i * i <= x:
                perfect.append(i * i)
                i += 1
            return perfect

        squares = count_squares(n)
        squares_set = set(squares)
        memo = {}

        def dp(x):
            if x < 0:
                return float('inf')
            if x == 0:
                return 0
            if x in squares_set:    
                return 1
            if x not in memo:
                least = float('inf')
                for square in reversed(squares):
                    if square > x:
                        continue
                    least = min(least,dp(x - square) + 1 )     
                memo[x] = least
            return memo[x]

        return dp(n)
