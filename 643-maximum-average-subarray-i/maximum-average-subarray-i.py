class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maximum = summ
        for r in range(len(nums)-k):
            summ = summ + nums[r+k] - nums[r]
            maximum = max(maximum, summ)
        maximum_ave = maximum/k
        return maximum_ave