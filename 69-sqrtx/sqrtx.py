class Solution:
    def mySqrt(self, x: int) -> int:
        def validate(n):
            return n*n <= x
        l = 0
        r = x
        ans = None
        while l <= r:
            m = (l+r)//2
            if validate(m):
                ans = m
                l = m+1
            else:
                r = m-1
        return ans 

            