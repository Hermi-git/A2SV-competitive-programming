class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(start, path):
            if len(path) == k:
                answer.append(path[:])
            
            for cand in range(start, n+1):
                if len(path) <= k:
                    path.append(cand)
                    backtrack(cand+1, path)
                    path.pop()
        
        backtrack(1, [])
        return answer