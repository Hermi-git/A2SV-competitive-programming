class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack[0: len(needle)]:
            return 0
        for i in range(1, len(haystack) - len(needle) +1):
            
            if needle == haystack[i:i + len(needle)]:
                return i
                break
        return -1