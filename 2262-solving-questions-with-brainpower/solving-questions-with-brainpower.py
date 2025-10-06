class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(index):
            if index >= len(questions):
                return 0
            if index not in memo:
                points, brainpower = questions[index]
                solve = points + dp(index + brainpower +1)
                skip = dp(index +1)
                memo[index] = max(solve, skip)
            return memo[index] 
        return dp(0)
