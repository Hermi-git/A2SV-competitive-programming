class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if abs(target - cur_sum) < abs(target-closest_sum):
                    closest_sum = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    l += 1
                else:
                    r -=1
        return closest_sum
                