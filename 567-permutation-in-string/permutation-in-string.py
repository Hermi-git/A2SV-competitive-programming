class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if s1_count == window:
            return True
        for r in range(len(s2)-len(s1)):
            window[s2[r+len(s1)]] += 1
            window[s2[r]] -= 1
            if s1_count == window:
                return True
        return False
