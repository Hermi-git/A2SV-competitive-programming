class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = sum([nums[i] for i in range(len(nums)) if i %2 == 0])
        odd = sum([nums[i] for i in range(len(nums)) if i %2 == 1])
        return even - odd