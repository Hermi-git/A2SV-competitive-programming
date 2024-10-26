class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =[]
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            elif k > 0 and nums[k] == nums[k-1]:
                continue            
            i, j = k + 1, len(nums)-1
            while i < j:
                summ = nums[i] + nums[j] +nums[k]
                if summ == 0:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i< j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif summ < 0:
                    i += 1
                else: 
                    j -=1
        return ans
