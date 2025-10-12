class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def dp(index, can_buy):
            if index == len(prices):
                return 0
            profit = 0
            if memo[index][can_buy] == -1:
                if can_buy:
                    buy= -prices[index] + dp(index+1, 0)
                    not_buy = dp(index+1, 1)
                    profit = max(buy, not_buy)
                else:
                    sell = prices[index] + dp(index+1, 1) - fee
                    not_sell = dp(index+1, 0)
                    profit = max(sell, not_sell)
                memo[index][can_buy] = profit 
            return memo[index][can_buy] 
        return dp(0, 1)