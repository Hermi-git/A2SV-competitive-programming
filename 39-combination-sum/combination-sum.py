class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                answer.append(path[:])
                return
            if remaining < 0:
                remaining = target
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return answer 