class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sn =0 
        for i in range(len(nums)):
            sn ^= nums[i]
        return sn
        