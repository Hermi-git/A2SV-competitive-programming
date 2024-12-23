class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            squaresum = l **2 + r**2
            if squaresum == c:
                return True
          
            elif squaresum > c:
                r -= 1
            else:
                l += 1
            
        return False





