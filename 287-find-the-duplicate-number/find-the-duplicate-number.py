class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            idx = nums[i] -1
            if nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]