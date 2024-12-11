class Solution:
    def maximumLength(self, s: str) -> int:
        subarr = []
        for i in range(len(s)):
            idx = i
            while idx < len(s) and s[idx] == s[i]:
                subarr.append(s[i:idx+1])
                idx +=1 
        
        count = Counter(subarr)
        longest = 0
        for sub, n in count.items():
            if n >= 3:
                longest = max(len(sub),longest)
        if longest == 0:
            return -1
        return longest


       
        