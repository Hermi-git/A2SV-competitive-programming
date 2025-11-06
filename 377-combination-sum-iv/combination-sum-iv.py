class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            total =0
            if remain not in memo:
                for num in nums:
                    total += dp(remain-num)
                    memo[remain] = total
            return memo[remain]
        return dp(target)
    