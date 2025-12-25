class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for idx, c in enumerate(s):
            result += (idx + 1) * (ord('z') - ord(c) + 1)
        return result

