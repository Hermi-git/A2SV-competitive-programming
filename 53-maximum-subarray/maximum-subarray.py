class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subsum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_subsum = max(max_subsum, current_sum)
        return max_subsum