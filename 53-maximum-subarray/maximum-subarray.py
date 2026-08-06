class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = nums[0]
        max_sofar = nums[0]

        for i in range(1, len(nums)):
            max_end = max(max_end + nums[i], nums[i])
            max_sofar = max(max_end, max_sofar)
        return max_sofar