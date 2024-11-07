class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i in range(len(s)):
            if s[i] in count:
                if count[s[i]] < 2:
                    return i
        return -1
        