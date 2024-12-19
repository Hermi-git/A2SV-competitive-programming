class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, summ= 10 ** 6, 0
        l = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                min_len = min(min_len, r -l + 1)
                summ -= nums[l]
                l += 1
        return 0 if min_len == 10**6 else min_len


