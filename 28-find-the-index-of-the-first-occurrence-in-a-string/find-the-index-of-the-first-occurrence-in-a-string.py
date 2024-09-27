class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle) -1
        while right < len(haystack):
            if haystack[left:right+1] == needle:
                return left
            else:
                left+=1
                right+=1
        return -1