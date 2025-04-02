class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        def backtrack(idx, path):
            subset.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            return
        backtrack(0, [])
        return subset

       