class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            idx = nums[i] -1
            if nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        answer = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                answer.append(nums[i])
                answer.append(i+1)
        return answer