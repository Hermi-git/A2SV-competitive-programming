class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for ch in r:
            if m[ch] < r[ch]:
                return False
        return True