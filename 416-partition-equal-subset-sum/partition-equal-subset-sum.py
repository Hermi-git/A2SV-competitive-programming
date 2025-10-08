class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(num for num in nums) 
        if total & 1:
            return False
        half = total // 2
        memo ={}
        def dp(i, summ):
            if summ == half:
                return True 
            if i >= len(nums):
                return False 
            if (i, summ) not in memo:
                memo[(i, summ)] = dp(i+1, summ + nums[i]) or dp(i+1, summ)
                
            return memo[(i, summ)] 
        return dp(0, 0)

