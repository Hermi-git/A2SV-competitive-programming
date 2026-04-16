class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(start, path):
            answer.append(path[:])

            for cand in range(start, len(nums)):
                if start != len(nums):
                    path.append(nums[cand])
                    backtrack(cand+1, path)
                    path.pop()
        backtrack(0, [])
        return answer
