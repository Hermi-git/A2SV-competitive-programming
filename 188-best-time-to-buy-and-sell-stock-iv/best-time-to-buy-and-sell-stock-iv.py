class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = [[[-1 for _ in range(k+1)]for _ in range(2)]for _ in range(len(prices))]
        def dp(index, can_buy, transaction):
            if index == len(prices) or transaction == 0:
                return 0
        
            if memo[index][can_buy][transaction] == -1:
                if can_buy:
                    buy = -prices[index] + dp(index+1, 0, transaction)
                    not_buy = dp(index+1, 1, transaction)
                    profit = max(buy, not_buy)
                else:
                    sell = prices[index] +dp(index+1, 1, transaction-1)
                    not_sell = dp(index+1, 0, transaction)
                    profit = max(sell, not_sell)
                memo[index][can_buy][transaction] = profit
            return memo[index][can_buy][transaction] 
        return dp(0, 1, k)