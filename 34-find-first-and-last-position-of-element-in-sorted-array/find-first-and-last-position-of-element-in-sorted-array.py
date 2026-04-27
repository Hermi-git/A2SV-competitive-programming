class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        first_pos =-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                first_pos = m
                r = m - 1
        if first_pos == -1 or nums[first_pos] != target:
            return [-1, -1]
        
        l = 0
        r = len(nums)-1
        right_pos = -1
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                right_pos = m
                r = m-1
            else:
                l = m+1
        right_pos = right_pos - 1 if right_pos != -1 else len(nums) - 1
        return [first_pos, right_pos]

       
            
                