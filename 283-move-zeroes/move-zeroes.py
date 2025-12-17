class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        for seek in range(len(nums)):
            if nums[seek] != 0:
                nums[holder], nums[seek] = nums[seek], nums[holder]
                holder += 1
        return nums

