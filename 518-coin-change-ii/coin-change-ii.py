class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        def dp(index, total):
            if total > amount:
                return 0
            if index == len(coins):
                if total == amount:
                    return 1
                else:
                    return 0
            
            if memo[index][total] == -1:
                memo[index][total] = dp(index, total + coins[index]) + dp(index+1, total)
            
            return memo[index][total]
            
        return dp(0,0)