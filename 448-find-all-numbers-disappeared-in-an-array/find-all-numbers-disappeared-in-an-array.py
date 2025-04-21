class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = min(nums)
        nums.sort()
        ans = []
        i = 0
        if minimum != 1:
            while minimum > 1:
                minimum -= 1
                ans.append(minimum)         
        if maximum != len(nums):  
            while maximum < len(nums):
                maximum += 1
                ans.append(maximum)
        while i < len(nums) - 1:  
            if nums[i] + 1 != nums[i + 1] and nums[i] != nums[i + 1]:
       
                ans.append(nums[i] + 1)
                nums.insert(i + 1, nums[i] + 1)  
            else:
                i += 1  
        return(ans)
