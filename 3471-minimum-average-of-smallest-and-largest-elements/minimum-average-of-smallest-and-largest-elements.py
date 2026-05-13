class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average = []
        nums.sort()
        l = 0
        r = len(nums)-1
        while l <= len(nums)//2 and r >= len(nums)//2:
            ave = (nums[l] + nums[r]) / 2
            average.append(ave)
            l += 1
            r -= 1
        return min(average) 