class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            idx = nums[i] -1

            if idx >= 0 and idx < len(nums) and nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
       

        
        