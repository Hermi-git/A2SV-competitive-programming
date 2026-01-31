class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = l = 0
        mini = float('inf')
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                mini = min(mini, r-l+1)
                summ -= nums[l]
                l += 1
        return mini if mini != float('inf') else 0
