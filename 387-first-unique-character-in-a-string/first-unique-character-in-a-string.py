class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for i in range(len(s)):
            if s_count[s[i]] == 1:
                return i
                break
        return -1
        