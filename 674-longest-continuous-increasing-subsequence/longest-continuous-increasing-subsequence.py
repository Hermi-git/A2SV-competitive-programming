class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n = len(nums)
        longest = 1
        currLen = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                currLen += 1
                longest = max(longest, currLen)
            else:
                currLen = 1
        return longest