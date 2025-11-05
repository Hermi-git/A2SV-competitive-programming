class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def dp(index, canbuy):
            if index >= len(prices):
                return 0
            profit = 0
            if memo[index][canbuy] == -1:
                if canbuy:
                    buy= -prices[index] + dp(index+1, 0)
                    not_buy = dp(index+1, 1)
                    profit = max(buy, not_buy)
                else:
                    sell = prices[index] + dp(index+2, 1)
                    not_sell = dp(index+1, 0)
                    profit = max(sell, not_sell)
                memo[index][canbuy] = profit
            return memo[index][canbuy] 
        return dp(0, 1)