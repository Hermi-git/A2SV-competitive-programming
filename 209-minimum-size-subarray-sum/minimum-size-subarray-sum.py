class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_size = float('inf')
        summ = 0
        for r in range(len(nums)):
            summ += nums[r] 
            while summ >= target:
                min_size = min(min_size, r - l + 1)
                summ -= nums[l]
                l += 1
        if min_size != float("inf"):
            return min_size
        else:
            return 0
            