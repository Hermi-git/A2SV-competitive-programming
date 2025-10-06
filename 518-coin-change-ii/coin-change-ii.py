class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        
        for index in range(len(coins)-1, -1, -1):
            for total in range(amount, -1, -1):
                take = memo[index][total + coins[index]] if total + coins[index] <= amount else 0
                skip = memo[index+1][total] if index +1 != len(coins) else total == amount

                memo[index][total] = take + skip
            
        return memo[0][0]