class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        res =0 
        while x:
            res *= 10
            res += x % 10
            x //= 10

        return temp == res