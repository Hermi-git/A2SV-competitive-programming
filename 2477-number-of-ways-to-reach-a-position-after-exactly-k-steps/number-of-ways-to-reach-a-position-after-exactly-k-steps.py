class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        d = abs(endPos - startPos)
        right = (k+d) // 2
        left = k - d
        if left % 2 != 0 or left <0:
            return 0
        return math.comb(k, right) % mod
 


        

