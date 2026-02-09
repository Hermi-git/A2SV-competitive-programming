class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path, open, close):
            if len(path) == 2*n:
                ans.append("".join(path[:]))
                return
            
            if open < n:
                path.append("(")
                backtrack(path, open+1, close+1)
                path.pop()

            if close > 0:
                path.append(")")
                backtrack(path, open, close-1)
                path.pop()

            return


        backtrack([], 0, 0)
        return ans