class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        x_rev = xs[::-1]
        if xs != x_rev:
            return False
        return True
        
        
        
        
        