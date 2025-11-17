class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int: 
        d = abs(endPos - startPos)
        r = (k+d)//2
        l = (k-d)
        if l % 2 != 0 or l <0:
            return 0
        return math.comb(k, r) % (10**9 + 7)
 


        

