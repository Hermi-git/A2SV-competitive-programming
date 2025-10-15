class Solution:
    def validStrings(self, n: int) -> List[str]:
        answer = []
        def backtrack(s):
            if len(s) == n:
                answer.append(s)
                return                      
            if not s or s[-1] == '1':
                backtrack(s + "0")
                backtrack(s + "1")
            else:  
                backtrack(s + "1")
        backtrack("")
        return answer
