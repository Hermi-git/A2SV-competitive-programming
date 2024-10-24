class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(s, l+1, r) or helper(s, l, r-1)
        return True