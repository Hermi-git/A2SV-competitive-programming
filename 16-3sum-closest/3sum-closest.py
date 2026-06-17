class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for k in range(len(nums)):
            l = k+1
            r = len(nums)-1
            while l < r:
                summ = nums[k] + nums[l] + nums[r]
                if abs(target - summ) < abs(target-closest):
                    closest = summ
                if summ == target:
                    return target
                if summ < target:
                    l += 1
                else:
                    r -= 1
        return closest

               
                