class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        ans = []
        
        def backtrack(i, dots, ip):
            remaining = n - i
            segments_left = 4 - dots
            if remaining < segments_left or remaining > 3 * segments_left:
                return
            if dots == 4:
                if i == n:
                    ans.append(ip[:-1])  
                return
            
            for j in range(i, min(i + 3, n)):
                part = s[i:j+1]
                if (part[0] == '0' and len(part) > 1):
                    break 
                val = int(part)
                if val <= 255:
                    backtrack(j+1, dots+1, ip + part + ".")
                if val > 255:
                    break
        
        backtrack(0, 0, "")
        return ans
