class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, total):
            if index == len(nums):
                return total
            
            include = backtrack(index+1, total ^ nums[index])
            exclude = backtrack(index+1, total)
            return include + exclude
        return backtrack(0, 0)