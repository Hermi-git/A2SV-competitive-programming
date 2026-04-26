class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(index, prev_prev,prev, count):
            if index == len(num):
                return count >= 3
            
            for i in range(index, len(num)):
                curr = num[index:i+1]
                if len(curr) > 1 and curr[0] =="0":
                    continue
                cur = int(curr)
                if prev_prev == None or  prev_prev + prev == cur:
                    if backtrack(i+1, prev, cur, count+1):
                        return True
            return False
        
        return backtrack(0, None, None, 0)

